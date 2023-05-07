# HTML Tutorial

- [HTML Tutorial](#html-tutorial)
- [1. Introduction to HTML](#1-introduction-to-html)
  - [Mega Tag](#mega-tag)
  - [Title Tag](#title-tag)
  - [Comments in HTML :](#comments-in-html-)
  - [VS Code Shortcuts](#vs-code-shortcuts)
  - [Practice Set :](#practice-set-)
- [2. Basic HTML Tags](#2-basic-html-tags)
  - [HTML Element:](#html-element)
  - [HTML Attributes:](#html-attributes)
  - [Heading Tag :](#heading-tag-)
  - [Paragraph Tag:](#paragraph-tag)
  - [Bold, Italic and Underline Tags:](#bold-italic-and-underline-tags)
  - [Big and Small Tag:](#big-and-small-tag)
  - [Subscript and Superscript :](#subscript-and-superscript-)
  - [pre tag :](#pre-tag-)
  - [Anchor Tag :](#anchor-tag-)
  - [Image Tag :](#image-tag-)
  - [Practice Set :](#practice-set--1)
- [3. Creating Page Layout](#3-creating-page-layout)


# 1. Introduction to HTML

- HTML is used for defining layout of a page - A bare bone page structure.

## Mega Tag

- Meta tag used in mainly SEO (search engine optimization) of the web page.

```html
<!-- Boiler Contains -->
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- You have to write your own -->
<meta name="description" content="This is description of the web page which shows in search engine in short.">
<meta name="keywords" content="html, html tutorial, web development">
<meta name="robots" content="NOINDEX, NOFOLLOW">

<!-- When you want to don't come in search engine. So, write always. -->
<meta name="robots" content="INDEX FOLLOW">
```

## Title Tag

```html
<title> HTML Tutorial</title>
```

- How to add external links for css page.
```html
<link rel="stylesheet" href="/style.css">
```

- How to add external JavaScript page.
```html
<script src="/script.js"></script>
```

## Comments in HTML :
- Comments in HTML are used to mark text which should not be parsed. They can help document the source code.
- **Shortcut -** `Ctrl` + `/`
```html
<!-- This is comment -->
```

## VS Code Shortcuts

- `Ctrl` + `Tab` to switch files in vs code.
- `Alt` + `Tab` to switch application in windows.
- `Ctrl` + `/` to comment and uncomment.
- `Alt` + `z` to toggle word wrap (all content visible).
- 

## Practice Set :
1. Inspect your favorite website and change something on the page which is displayed.
2. Go to your favorite website and try to view the page source and write the exact lines of code. Does it clone the website? why?

# 2. Basic HTML Tags

## HTML Element:

- Everything contains from starting tag to the ending tag.

## HTML Attributes:

- Used to add more information corresponding to an HTML tag.
- More than one attributes can be use in a tag.

__Example : Anchor Tag - href attribute__

```html
<a href="https://google.com"> Google </a>
```
- We can either use single or double quote in attributes.
- **Shortcut to multiple cursor:** `Alt` + `Click`.

## Heading Tag :
- Heading tag is used to mark headings in HTML.
- From h1 to h6, we have tags for the most important to the least important headings. (Readability decreases).

```html
<h1> Most Important Heading </h1>
<h2> 2nd Most Heading H2 </h2>
<h3> 3rd Most Heading H3 </h3>
<h4> Heading H4 </h4>
<h5> Heading H5 </h5>
<h6> Heading H6 </h6>
```
- **Note :** Don't use HTML headings to make bold.

## Paragraph Tag:
- Paragraph tags are used to add paragraphs to an HTML page.
- Shortcuts to create multiple paragraph `p*4` Enter.

```html
<p> This is a paragraph </p>
```

## Bold, Italic and Underline Tags:
- We can use `bold`, `italic` and `underline` tags.

___`Bold` and `Strong` Tag:__ Bold a line/word.

```html
<b> This is Bold </b>
<!-- strong tag -->
<!-- It recommended to use it not bold tag -->
<strong>This is strong/bold.</strong>
```

__*Italic* and *Emphasize* Tag:__

```html
<i> This is italic </i>

<!-- emphasize tag -->
<em> Emphasize Tag </em> 
```

__<u>Underline</u> Tag:__

```html
<u> This is underline </u>
```
- **Note :** You can't create extra spaces or lines in between tags's content by writing in code this does not work - To o this ->

__br tag:__
```html
<br>
```
  - br tag is used to create line breaks in an HTML.
  - Extra spaces are ignored.
  - Self closing tag.


__hr tag__:
```html
<hr>
```
  - hr tag is used to create a horizontal ruler after used to separate the content.
  - Self closing tag.

<hr>

## Big and Small Tag:

* We can make the text a bit longer and a bit smaller using big and small tags respectively.

<big> Big Tag </big>
```html
<big> This is big </big>
```

<small> Small Tag </small>
```html
<small>This is small<small>
```

## Subscript and Superscript :
* We can add subscript and superscript in HTML as follows :

__Subscript :__ CO<sub>2</sub>
```html
<sub> Subscript <sub>
```

__Superscript :__ 10<sup>5<sup>
```html
<sup> Superscript </sup>
```

## pre tag :

HTML always ignores extra and newlines. In order to display a piece of text as it is, we use pre tag.

```html
<pre>
    This is written
        using pre
            tag
</pre>
```
* Example is shown as below:

<pre>This is written
      as it is
      using pre tag
</pre>

## Anchor Tag :
- Anchor tag is used to add links to an existing content inside an HTML page.
- ##### Example of absolute link - (Globally can be access)

```html
<a href="https://google.com"> Click Google </a>
```

- **Example** of relative link - (Only on server access)

```html
<a href="2-about.html"> Go to about </a>
```

## Image Tag :
* img tag is used to add images in an HTML page
* Take open source image api [Unsplash Online Images](https://unsplash.com/)
* `alt` attribute is use to display massage when image not loaded.

__Example of Relative url of an image:__
```html
<img src="image.jpg" alt="Loading Error">
```

__Example of Absolute url of an image:__
```html
<img src="https://images.unsplash.com/photo-1660068226910-2e18eb033f1d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1888&q=80" alt="Human Image">
```

## Practice Set :
1. Create an HTML page with a heading (title heading), a primary heading and a subheading. Which tag did you use?
2. Create a page with 5 wallpapers images taken from the internet.
3. Use br and hr tags to display a piece of text with line breaks
4. Try to write the following chemical equation using HTML.
   - Example : C + O<sub>2</sub> &rarr; CO<sub>2</sub>
   - Hint: [HTML arrow](https://www.w3schools.com/charsets/ref_utf_arrows.asp)
5. Try to write a wikipedia article using HTML.


# 3. Creating Page Layout

