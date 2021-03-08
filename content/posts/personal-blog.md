---
title: "Personal Blog"
date: 2021-03-06T16:27:28-08:00
draft: false
toc: true
images:
tags:
  - intro
---

# Overview
This is personal blog power by hugo hosted on github pages

# Setup procedure

Follow the steps in [Hugo - Quick Start](https://gohugo.io/getting-started/quick-start/)

On MacBook install `hugo`

```bash
brew install hugo
```

Create a new personal blog site
```bash
hugo new site zshen-blog
```

Choose a theme, and add it as submodule

```bash
git submodule add https://github.com/rhazdon/hugo-theme-hello-friend-ng.git themes/hello-friend-ng
```

Copy the exampleSite files into git repo root folder, remove the existing posts

```bash
cp themes/hello-friend-ng/exampleSite/* ./
rm content/posts/*
```

Create a new post
```
hugo new posts/my-first-post.md
```

# How to automate?

source code is committed to `main` branch
use GitHub actions to automate the deployment to `gh-pages` branch


## Reference
- [HUGO - Quick Start](https://gohugo.io/getting-started/quick-start/)
- [HUGO - Host on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
- [GitHub - hugo-theme-hello-friend-ng](https://github.com/rhazdon/hugo-theme-hello-friend-ng)