/**
 * Estimate reading time for a given text body.
 *
 * @param body - Raw text content (Markdown/MDX source)
 * @param wpm  - Reading speed in words per minute (default: 200)
 * @returns Estimated reading time in minutes (minimum 1)
 */
export function readingTime(body: string, wpm = 200): number {
  const cjk = /[\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Hangul}]/gu;
  const characterCount = (body.match(cjk) ?? []).length;
  const words = body.replace(cjk, ' ').trim().split(/\s+/).filter(Boolean).length;
  const wordCount = characterCount + words;
  return Math.max(1, Math.ceil(wordCount / wpm));
}
