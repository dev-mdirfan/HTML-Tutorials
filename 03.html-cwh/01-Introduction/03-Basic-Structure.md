# 03 Basic Structure

## Basic Structure of a Website

- Press `!` + `Enter`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- This is Body of html -->
</body>
</html>
```

- This is the code which is required to make a html file.

### Explanation

#### Line 1 : DocType

```html
<!-- A -->
<!DOCTYPE html>
```

- It tells, this document is a HTML document.
- Types of documents browser can understand :
  - **HTML**
  - **XHTML**

#### What is a Tag

- So basically if we open a tag we have to close it also by angular bracket (< >).

```html
<html lang="en">    <!-- Opening Tag -->

</html>             <!-- Closing Tag -->
```

- It has a attribute name : `lang` that means language of the html page.

##### Inside HTML

1. `head` Tag
2. `body` Tag

```html
<head>
    <!-- Inside head tag -->
</head>

<body>
    <!-- Inside body tag -->
</body>
```

- Now lets understand what is included in head and body.

#### Inside Head Tag

- `head` includes all the meta tags which we write to describe a website.
  1. Metadata
  2. Title
  3. link or any External sheet (css).

##### What is meta Tag

- `meta` means information about information.
- Metadata is data that provides information about other data.
- There are keywords and description which helps in telling all this things.
- Many distinct : descriptive metadata, structural metadata, administrative metadata, reference metadata, and statical metadata.
