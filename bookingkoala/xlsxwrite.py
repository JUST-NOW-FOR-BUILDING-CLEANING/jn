"""Minimal .xlsx writer (no third-party packages): multiple sheets, inline strings, numbers,
formulas (Excel syntax), a few cell styles, column widths, row heights, frozen header, autofilter."""
import zipfile, html
from xml.sax.saxutils import escape

STYLES = ["body", "bold", "title", "note", "hdr", "input", "ar"]
def col(n):
    s = ""
    while n: n, r = divmod(n - 1, 26); s = chr(65 + r) + s
    return s

class Sheet:
    def __init__(self, name, widths, freeze=None, autofilter=None):
        self.name, self.widths, self.rows, self.freeze, self.autofilter = name, widths, [], freeze, autofilter
    def add(self, cells, height=None): self.rows.append((cells, height))

def sheet_xml(sh):
    out = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">']
    if sh.freeze:
        out.append(f'<sheetViews><sheetView workbookViewId="0"><pane ySplit="{sh.freeze-1}" topLeftCell="A{sh.freeze}" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
    out.append('<sheetFormatPr defaultRowHeight="15"/>')
    out.append("<cols>" + "".join(f'<col min="{i+1}" max="{i+1}" width="{w}" customWidth="1"/>' for i, w in enumerate(sh.widths)) + "</cols>")
    out.append("<sheetData>")
    for ri, (cells, height) in enumerate(sh.rows, 1):
        ht = f' ht="{height}" customHeight="1"' if height else ""
        out.append(f'<row r="{ri}"{ht}>')
        for ci, c in enumerate(cells, 1):
            if c is None: continue
            v, kind = c
            if v is None or v == "": continue
            ref = f"{col(ci)}{ri}"
            s = STYLES.index(kind if kind in STYLES else "body")
            if kind == "num": out.append(f'<c r="{ref}" s="{s}"><v>{v}</v></c>')
            elif kind == "formula":
                f, cached = (v if isinstance(v, tuple) else (v, None))
                if isinstance(cached, (int, float)): out.append(f'<c r="{ref}" s="{s}"><f>{escape(str(f))}</f><v>{cached}</v></c>')
                else: out.append(f'<c r="{ref}" s="{s}" t="str"><f>{escape(str(f))}</f><v>{escape(str(cached or ""))}</v></c>')
            else: out.append(f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(str(v))}</t></is></c>')
        out.append("</row>")
    out.append("</sheetData>")
    if sh.autofilter: out.append(f'<autoFilter ref="{sh.autofilter}"/>')
    out.append("</worksheet>")
    return "".join(out)

STYLES_XML = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<fonts count="6">
<font><sz val="10"/><name val="Arial"/></font>
<font><b/><sz val="10"/><name val="Arial"/></font>
<font><b/><sz val="14"/><name val="Arial"/></font>
<font><i/><sz val="10"/><color rgb="FF555555"/><name val="Arial"/></font>
<font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Arial"/></font>
<font><sz val="10"/><color rgb="FF0000FF"/><name val="Arial"/></font>
</fonts>
<fills count="4"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FF0B6F78"/></patternFill></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FFFFF2CC"/></patternFill></fill></fills>
<borders count="2"><border><left/><right/><top/><bottom/><diagonal/></border>
<border><left style="thin"><color rgb="FFCCCCCC"/></left><right style="thin"><color rgb="FFCCCCCC"/></right><top style="thin"><color rgb="FFCCCCCC"/></top><bottom style="thin"><color rgb="FFCCCCCC"/></bottom><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="7">
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="0" fontId="1" fillId="0" borderId="1" applyFont="1" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="0" fontId="2" fillId="0" borderId="0" applyFont="1"/>
<xf numFmtId="0" fontId="3" fillId="0" borderId="0" applyFont="1" applyAlignment="1"><alignment wrapText="0" vertical="top"/></xf>
<xf numFmtId="0" fontId="4" fillId="2" borderId="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="0" fontId="5" fillId="3" borderId="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf>
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="top" horizontal="right" readingOrder="2"/></xf>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>'''

def write(path, sheets):
    z = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)
    z.writestr("[Content_Types].xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        + "".join(f'<Override PartName="/xl/worksheets/sheet{i+1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(len(sheets))) + "</Types>")
    z.writestr("_rels/.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    z.writestr("xl/workbook.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
        + "".join(f'<sheet name="{escape(s.name)}" sheetId="{i+1}" r:id="rId{i+1}"/>' for i, s in enumerate(sheets)) + '</sheets><calcPr fullCalcOnLoad="1"/></workbook>')
    z.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        + "".join(f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i+1}.xml"/>' for i in range(len(sheets)))
        + f'<Relationship Id="rId{len(sheets)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>')
    z.writestr("xl/styles.xml", STYLES_XML)
    for i, s in enumerate(sheets): z.writestr(f"xl/worksheets/sheet{i+1}.xml", sheet_xml(s))
    z.close()
