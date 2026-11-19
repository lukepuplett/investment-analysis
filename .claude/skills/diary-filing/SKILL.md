---
description: File things the user posts into the current month's journal (diary/YYYY-MM.md). Use when the user posts an image (screenshot of a tweet, newspaper clipping, chart, press cutting) or pastes text that reads like a tweet/X post or a press clipping (handle, likes/views, dateline, byline, "(Reuters) -", press-release boilerplate). Also when they say "file this", "diary this", "add to the journal". Creates the month's file if it doesn't exist.
allowed-tools: Bash, Read, Edit, Write, Grep
---

File what the user posted into `diary/YYYY-MM.md` in this repo, matching the existing entries. Don't comment on it, fact-check it or draw links to the portfolio unless they ask. Finish by committing and pushing (step 6).

Now (UK time): !`TZ=Europe/London date '+%Y-%m-%d %H:%M'`

## When to act, and when not to

- **Image posted:** read the text off the image and file it. If the image is clearly about the task in hand (an error, a terminal, a chart of our own model output) and not a clipping to keep, don't file it. If it's unclear which, ask in one line.
- **Pasted text:** file it when it reads like a tweet/X post (handle, @mentions, $TICKERs, engagement counts, short punchy lines) or a press clipping (headline, byline, dateline, wire tag, press-release boilerplate). Don't file instructions, questions, code, or ordinary chat.
- **The user's own writing** (their post, essay, note) goes in too when they say it is theirs; use `Luke's thinking:` in the heading, as the existing entries do.

## Steps

1. **Month file.** Use the month from the date above: `diary/YYYY-MM.md`. If it doesn't exist, create it starting with `# Diary — Month YYYY` (for example `# Diary — December 2026`), then a blank line. Never rewrite or reorder existing entries.
2. **Duplicates.** Grep the month file (and the previous month's) for a distinctive phrase from the post. If it's already filed, say so and stop.
3. **Image file.** If the image exists on disk (a path in the message or the pasted-image cache), copy it to `diary/assets/` as `YYYY-MM-DD-<source>-<topic-slug>.<ext>` (lowercase, hyphens). If the image can't be reached as a file, file the text without the image link and tell the user the picture wasn't saved.
4. **Transcribe faithfully.** Copy the text word for word into a blockquote, keeping paragraph breaks, numbers, tickers and emoji. Remove only page chrome (menus, "Show more", ad slots). If part of an image is unreadable, write `[unreadable]`. Don't fix spelling, add facts, or fill in a name that isn't visible; if the author is unclear, write `source unclear`.
5. **Append the entry at the end of the file**, in this shape:

```markdown
### YYYY-MM-DD HH:MM — <Author or outlet>: <short plain-English headline>

Source: <author/handle or outlet, platform, date if shown>. Posted by Luke as <screenshot / pasted text / newspaper clipping>.

![<alt text describing the image>](assets/<filename>)

> <verbatim text, one blockquote paragraph per paragraph>

Tags: #Author #TICKER #Topic
```

   - Time is the UK time above. Headline is a short label for what was said, in plain words.
   - Leave out the image line for text-only posts.
   - Add a `See also:` line only when an earlier entry in the same file is obviously about the same thing, naming it by its heading.
   - Tags: author or outlet, tickers mentioned, two or three topics.
   - Use they/them for any person whose pronouns the post doesn't state.
6. **Commit and push on completion.** The user has authorised this for diary filings, so don't ask first.
   - Stage only the files this filing touched: the month file and the new image in `diary/assets/`. Never `git add -A`, and never stage anything else that happens to be modified.
   - Commit with the message `diary: file <source> clip on <topic>` (for a month file you created, the same message is fine), ending with the attribution trailer the session gives for commits.
   - Run `git pull --rebase` and then `git push origin master`. Never force-push. If the rebase conflicts or the push is rejected, stop, leave the commit local, and tell the user what happened.
7. **Report in one or two lines:** the file, the entry heading, whether the image was saved, and the commit and push result. If a new month file was created, say so.

## Don't

- Don't commit or push anything outside a diary filing, and don't bundle unrelated changes into the diary commit.
- Don't add checks, commentary or analysis to the entry unless the user asks.
- Don't touch other months' files, other folders, or anything outside `diary/`.
