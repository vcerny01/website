---
layout: article
title: Notes on Note-Taking
date: 2021-06-03
toc: true
---

> “Creativity is just connecting things. When you ask creative people how they did something, they feel a little guilty because they didn't really do it, they just saw something. It seemed obvious to them after a while.” --- Steve Jobs

> "Nature does nothing in vain, and in the use of means to her goals she is not prodigal. Her giving to man reason and the freedom of the will which depends upon it is clear indication of her purpose. Man accordingly was not to be guided by instinct, not nurtured and instructed with ready-made knowledge; rather, he should bring forth everything out of his own resources." --- Immanuel Kant

<br>

In the past two years, lots of new note-taking apps emerged. I've been using Roam Research and Obsidian for more than two years now. This my reflection and collection of resources on this topic.

## What Changed

Let's take a look at [Evernote](https://evernote.com/) as an example of the standard note-taking paradigm.

Taking notes in Evernote is not very different from taking notes on paper. You have notebooks, each for a different use case, with your notes. At best, you have something like tags and _notebook stacks_. That seems okay, but as your database grows, it becomes a robust archive, something like a library. There is a certain hierarchical structure imposed in which isolated pieces of knowledge reside.

An example of a bit more advanced note-taking paradigm is [Wikipedia](https://wikipedia.org/) ([MediaWiki](https://en.wikipedia.org/wiki/MediaWiki)). There's no hierarchical structure between notes. Instead, notes are connected by links. Some notes are grouped using tags.

Each database is like a garden. The content and structure of gardens differ based on the preferences of the _gardeners_. Aside from public gardens, like Wikipedia, some people have created their own digital gardens. Learn more and check out some of them [here](https://github.com/MaggieAppleton/digital-gardeners).

Some note-taking paradigms go even further. For example the [Zettelkasten Method](https://en.wikipedia.org/wiki/Zettelkasten).

Until quite recently most apps operated within the standard note-taking paradigm (notes in notebooks). Luckily, with new tools being created, other note-taking paradigms are finding their way into the mainstream.

## Tools

Choosing the right note-taking app can be a daunting task, so, to save you some time, I reviewed some of the new apps I've had some experience with.

### [Roam Research](https://roamresearch.com/)

Roam introduces two rather new concepts into note-taking. Block-based note-taking and [backlinking](https://en.wikipedia.org/wiki/Backlink).

A block is basically a short paragraph, a bullet point. Blocks can be organized in a hierarchy. Pages are just collections of blocks.

Features:

- Block-based note-taking
- Primarily cloud-based
- [#roamcult](https://tobiasbru.medium.com/the-history-of-roam-research-and-the-roamcult-4c1e1897633d)
- Your graph is stored in [edn](https://github.com/edn-format/edn), exports to markdown, JSON, etc. are possible and encouraged, though
- Closed source
- $15/m (no free tier, you can apply for a scholarship, though)
- Some community plugins and themes
- Currently in beta

### [Obsidian](https://obsidian.md/)

Obsidian's _vault_ is a root directory for your notes. Notes in Obsidian are just markdown files. You can group them into folders, link between them, etc. While Obsidian has lots of amazing features and plugins (including backlinks), blocks are not possible in Obsidian.

Features:

- Based on markdown files
- Primarily self-hosted (syncing is easy, though)
- [Big community](https://forum.obsidian.md/), growing fast
- Closed source
- Free for personal use (paid sync, publish and commercial tiers)
- Lots of community plugins and themes
- Currently in beta

### [Athens Research](https://github.com/athensresearch/athens)

Open source alternative to Roam Research.

Features:

- Block-based note-taking
- Primarily self-hosted
- Open source with a copyleft license
- Rather small community
- Your graph is stored in edn, exports are possible
- Free (paid hosted options should be available soon)
- Virtually no plugins and themes
- Currently in beta

### [Logseq](https://logseq.com/)

Open source note-taking app aiming for a Roam-like experience based on plain text markdown/org-mode files.

Features:

- Block-based note-taking
- Primarily self-hosted (easy sync options)
- Free
- Open source with a copyleft license
- Your graph is stored in markdown/org-mode files (they look kinda weird, though)
- Small community, growing fast
- Some plugins and themes are available
- Currently in beta

---

Other software, such as [org-roam](https://www.orgroam.com/), [Remnote](https://www.remnote.io/), [TiddlyWiki](https://tiddlywiki.com/) or [Zettlr](https://www.zettlr.com/) should be mentioned as well.

## Why Does It Matter

Notes can be more than just _archives of information_. When you write your notes, you develop and clarify ideas. By ordering or linking your notes, you are actually connecting different ideas. Writing and thinking are complementary.

And that's not all. You can always combine your note-taking with other [tools for thought](https://numinous.productions/ttft/).

I would not say I'm building a _second brain_ with my notes. I'm just [augmenting](https://www.youtube.com/watch?v=KmuP8gsgWb8) my thinking.

## Resources

- [How to Take Smart Notes](https://www.goodreads.com/en/book/show/34507927-how-to-take-smart-notes) - book about the Zettelkasten method by Sönke Ahrens
- [The Thread of Threads on Roam Research](https://twitter.com/conaw/status/1198399750032232449?lang=en) - about the vision behind Roam by its founder
- [Roam: Why I Love It and How I Use It](https://www.nateliason.com/blog/roam) - article about Roam Research by Nat Eliason
- [Articles on Roam by Ness Labs](https://nesslabs.com/tag/roam) - some useful Roam tips
- [Linking Your Thinking](https://www.youtube.com/channel/UC85D7ERwhke7wVqskV_DZUA/videos?view=0&sort=p) - channel dedicated to note-taking with Obsidian
- [Andy Matuschak's notes](https://notes.andymatuschak.org/About_these_notes) - about evergreen notes
- [Roam Research: Revoluční zápiskovací aplikace](https://adamkrivka.cz/blog/roam/) - czech article about Roam by Adam Křivka
- [Semilattice](https://www.semilattice.xyz/) - collection of system and interaction concepts for personal knowledge management tools

I might add more resources later.

## Why I Use Roam Research

Currently, I'm using Roam Research. It all comes down to the workflow I have with each app. And the workflow I have with Roam Research is by far the most comfortable. The thing is that Roam doesn't require me to _keep track_. I didn't have to come up with a complex organizational structure. I just write. My notes have normal names. Well, I have a list of tags, but other than that, I simply write and make links and that's it.

Compared to other apps, my workflow with Roam is more focused and clean.

---

Regardless of how you take your notes, I highly encourage you to make some of your notes [public](https://www.swyx.io/learn-in-public/).