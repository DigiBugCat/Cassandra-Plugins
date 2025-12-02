---
name: yt-cli
description: Download and transcribe YouTube videos with speaker diarization and auto-chapters. Use when the user wants to transcribe a video URL, search YouTube for videos, list videos from a channel, search existing transcripts, list transcribed videos, read transcript content, or check if a video has already been transcribed.
---

# yt-cli

CLI tool for downloading and transcribing videos using yt-dlp and AssemblyAI.

## Commands

### Search YouTube for videos
```bash
yt-cli yt-search '<query>' [-n limit]
```
Search YouTube for videos matching the query. Returns video titles, channels, durations, view counts, and URLs.

Options:
- `-n, --limit <LIMIT>` - Maximum results to return (default: 10)

Example output:
```
Found 10 result(s) for 'rust tutorial':

1. Rust Programming Tutorial - Fireship (12:34)
   1.2M views
   https://youtube.com/watch?v=...

2. Learn Rust in 10 Minutes - TechChannel (10:15)
   500K views
   https://youtube.com/watch?v=...
```

Use the returned URLs with `yt-cli transcribe <url>` to transcribe a video.

### Transcribe a video

**IMPORTANT**: Transcription can take several minutes depending on video length. Always run in the background:

```bash
# Start transcription in background
yt-cli transcribe '<video-url>'
```
Use Bash tool with `run_in_background: true` to start the transcription.

Then poll for completion using BashOutput every 15-30 seconds until complete. The command will output progress updates as it downloads and transcribes.

Downloads audio, transcribes with speaker labels and auto-chapters, saves to `~/.yt-transcribe/transcripts/{platform}/{channel}/{video_id}/`.

Output includes: `transcript.md`, `transcript.json`, `metadata.json`, and the audio file.

### Check if video is already transcribed
```bash
yt-cli get '<video-url>'
```
Returns the transcript path if it exists. Use this before transcribing to avoid duplicates.

### Search transcripts
```bash
yt-cli search 'query' [-n limit]
```
Full-text search across all transcripts, descriptions, and chapter summaries.

### List channel videos
```bash
yt-cli channel '<channel-url>' [-n limit]
```
List latest videos from a YouTube channel. Takes a channel URL (e.g., `https://youtube.com/@CHANNEL`) or channel ID.

Options:
- `-n, --limit <LIMIT>` - Maximum videos to show (default: 20)

### List transcripts
```bash
yt-cli list [-p platform] [-c channel] [-H handle]
```
List all transcribed videos with optional filtering by platform, channel display name (`-c`), or channel handle (`-H`, e.g., `@EconomicsUnmasked`).

### Read a transcript
```bash
yt-cli read <path> [--json]
```
Output transcript content. Use `--json` for structured data with timestamps.

### Show statistics
```bash
yt-cli stats
```
Display total transcripts, channels, duration, and word counts.

### Reindex database
```bash
yt-cli reindex
```
Rebuild the search index from existing transcript files.

## Transcript Format

The markdown transcript includes:
1. **Chapters section** - Auto-generated summaries with timestamps
2. **Transcript section** - Speaker-labeled paragraphs with timestamps

Example:
```markdown
## Chapters

### [00:00] Introduction to the topic
Summary of what's discussed in this section...

### [05:23] Main discussion points
Summary of the main content...

---

## Transcript

**Speaker A** [00:00]: Welcome to the show...

**Speaker B** [01:23]: Thanks for having me...
```

## Storage Structure

```
~/.yt-transcribe/
├── transcripts/
│   └── youtube/
│       └── channel-name/
│           └── video-id/
│               ├── transcript.md
│               ├── transcript.json
│               ├── metadata.json
│               └── audio.m4a
└── yt-transcribe.db
```
