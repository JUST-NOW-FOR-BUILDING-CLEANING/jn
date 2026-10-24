// Creates the zone-specific package variables in BookingKoala.
// usage: node bkvars.mjs [limit] [startIndex] [--dry]

const ZONES = { A: [1, 2], B: [3, 4], C: [5], E: [6], D: [7] };
// [zone] -> { kitchen:[p1,p2,p3], studio, bhk1, bhk2, bhk3, villa4, villa5 }
const P = {
  A: { kitchen: [249, 329, 419], bhk1: [379, 499, 629], bhk2: [499, 629, 749], bhk3: [669, 839, 999], villa4: [999, 1259, 1499], villa5: [1679, 1999, 2349] },
  B: { kitchen: [279, 369, 459], bhk1: [409, 549, 689], bhk2: [549, 689, 819], bhk3: [729, 919, 1099], villa4: [1099, 1379, 1649], villa5: [1839, 2199, 2569] },
  E: { kitchen: [309, 409, 509], bhk1: [459, 609, 759], bhk2: [609, 759, 909], bhk3: [809, 1009, 1209], villa4: [1209, 1519, 1819], villa5: [2019, 2419, 2829] },
  C: { kitchen: [329, 439, 549], bhk1: [499, 659, 829], bhk2: [659, 829, 989], bhk3: [879, 1099, 1319], villa4: [1319, 1649, 1979], villa5: [2199, 2639, 3079] },
  D: { kitchen: [439, 549, 659], bhk1: [499, 659, 829], bhk2: [659, 829, 989], bhk3: [879, 1099, 1319], villa4: [1319, 1649, 1979], villa5: [2199, 2639, 3079] },
};
const SIZES = [
  // key, label, cleaners, hours (zone D kitchen/studio shifted +1)
  ["studio", "Studio", 2, [3, 4, 5]],
  ["bhk1", "1 BHK", 3, [3, 4, 5]],
  ["bhk2", "2 BHK", 3, [4, 5, 6]],
  ["bhk3", "3 BHK", 4, [4, 5, 6]],
  ["villa4", "Villa 4 BR", 6, [4, 5, 6]],
  ["villa5", "Villa 5+ BR", 8, [5, 6, 7]],
];
export const VARS = [];
for (const z of ["A", "B", "C", "E", "D"]) {
  const kh = z === "D" ? [4, 5, 6] : [3, 4, 5];
  P[z].kitchen.forEach((price, i) => VARS.push({ zone: z, cat: "4", svc: 0, name: `2 cleaners × ${kh[i]} hours – AED ${price}`, price, hours: kh[i] }));
  for (const [key, label, cl, hrs0] of SIZES) {
    const hrs = key === "studio" && z === "D" ? [4, 5, 6] : hrs0;
    const prices = key === "studio" ? P[z].kitchen : P[z][key];
    prices.forEach((price, i) => VARS.push({ zone: z, cat: "5", svc: 1, name: `${label} – ${cl} cleaners × ${hrs[i]} hours – AED ${price}`, price, hours: hrs[i] }));
  }
}

