import fs from "node:fs/promises";
import path from "node:path";
import fg from "fast-glob";
import sharp from "sharp";

const SOURCE_DIR = "Fotos";
const OUT_FULL_DIR = "Fotos/full";
const OUT_THUMB_DIR = "Fotos/thumb";
const MANIFEST = "gallery.json";

const FULL_MAX_W = 1600;
const THUMB_MAX_W = 520;
const WEBP_QUALITY = 78;

await fs.mkdir(OUT_FULL_DIR, { recursive: true });
await fs.mkdir(OUT_THUMB_DIR, { recursive: true });

const files = await fg(["**/*.{jpg,jpeg,png,JPG,JPEG,PNG}"], {
  cwd: SOURCE_DIR,
  onlyFiles: true,
  ignore: ["full/**", "thumb/**"]
});

files.sort();

const entries = [];
for (const rel of files) {
  const srcPath = path.join(SOURCE_DIR, rel);
  const base = path.parse(rel).name;

  const fullOut = path.join(OUT_FULL_DIR, `${base}.webp`);
  const thumbOut = path.join(OUT_THUMB_DIR, `${base}.webp`);

  await buildWebpIfNeeded(srcPath, fullOut, FULL_MAX_W, WEBP_QUALITY);
  await buildWebpIfNeeded(srcPath, thumbOut, THUMB_MAX_W, WEBP_QUALITY);

  entries.push({
    id: base,
    full: `Fotos/full/${base}.webp`,
    thumb: `Fotos/thumb/${base}.webp`
  });
}

await fs.writeFile(MANIFEST, JSON.stringify(entries, null, 2), "utf8");
console.log(`✅ Built ${entries.length} images -> ${MANIFEST}`);

async function buildWebpIfNeeded(src, out, maxW, quality) {
  try {
    const [s, o] = await Promise.all([fs.stat(src), fs.stat(out)]);
    if (o.mtimeMs >= s.mtimeMs) return;
  } catch {}

  const img = sharp(src).rotate();
  const meta = await img.metadata();

  let pipeline = img;
  if (meta.width && meta.width > maxW) {
    pipeline = img.resize({ width: maxW, withoutEnlargement: true });
  }

  await pipeline.webp({ quality, effort: 5 }).toFile(out);
}
