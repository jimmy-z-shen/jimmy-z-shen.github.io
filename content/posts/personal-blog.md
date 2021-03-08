---
title: "Personal Blog powered by Hugo"
date: 2021-03-06T16:27:28-08:00
draft: false
toc: true
images:
tags:
  - intro
---

## Overview

This personal blog is powered by `hugo`, build with `GitHub Actions` and hosted on `GitHub Pages`

## Setup Procedure

This is overall view of what's going to happen after the setup is all done

![workflow](/img/hugo-blog.svg)

### Preparation

Follow the steps in [GitHub Pages](https://pages.github.com/) and create a personal site repository:

* [jimmy-z-shen/jimmy-z-shen.github.io](https://github.com/jimmy-z-shen/jimmy-z-shen.github.io)

On MacBook install `hugo`
```bash
brew install hugo
```

### Initialize a personal blog

Create a new blog site locally
```bash
hugo new site zshen-blog
```
Choose a theme, and add it as submodule
```bash
git submodule add https://github.com/rhazdon/hugo-theme-hello-friend-ng.git themes/hello-friend-ng
```
Copy the `exampleSite` files into git repo root folder, remove the pre-defined posts
```bash
cp themes/hello-friend-ng/exampleSite/* ./
rm content/posts/*
```
Create a new post, add content to it
```bash
hugo new posts/hugo-blog.md
```
Push the initial commit to the personal GitHub site repo
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/jimmy-z-shen/jimmy-z-shen.github.io.git
git push origin main
```

### Auto publish with GitHub Actions

Create a GitHub action configuration file `.github/workflows/gh-pages.yml`

Use the default configuration in [build-hugo-with-github-action](https://gohugo.io/hosting-and-deployment/hosting-on-github/#build-hugo-with-github-action)

After we pushed this configuration file. GitHub Actions will help us generate the static site using we has been checked in to `main` branch and push to `gh-pages` branch

Note: Make sure in the GitHub [repo settings](https://github.com/jimmy-z-shen/jimmy-z-shen.github.io/settings), it's set to use `gh-pages` branch as the source

## Reference
- [HUGO - Quick Start](https://gohugo.io/getting-started/quick-start/)
- [HUGO - Host on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
- [GitHub - hugo-theme-hello-friend-ng](https://github.com/rhazdon/hugo-theme-hello-friend-ng)
- [Blog - Hugo GitHub Actions](https://www.imeetyou.net/post/2020/hugo-github-actions/)