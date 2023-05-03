---
title: Chapter 1
description: Chapter 1
weight: 43
emogi: 🤕
type: chapters
chapter: 1
section_start: Section 1
section_emogi: 🤠
---


<time datetime="2013-04-06T12:32+00:00">2 weeks ago</time>


```py
print("Hello World")
```


```js

import '/styles/globals.css'
import '/styles/globals.scss'
import ApplyTheme from '/features/theme';
import Navigation from '/components/navigation';
import Layout from '../layouts/basiclayout';
import { HeaderProvider } from '../contexts/headercontext';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {

  return (
    <html lang='en'>
      <body className='bg-[var(--dev-bg-colour)] scrollbar'>
        <ApplyTheme />
        <Navigation />
        <HeaderProvider>
          <Layout>
            {children}
          </Layout>
        </HeaderProvider>
      </body>
    </html>
  )
}


```



H~2~O


1. This is a numbered list
2. This is a numbered list
3. This is a numbered list
4. This is a numbered list
- This is a list
- This is a nested list
	- This is a nested list
		- This is a nested list
			- This is a nested list
				- This is a nested list


> This is a blockquote

> Quote: facts doesn`t cares feelings 

> This is a nested blockquote

>> This is a nested blockquote

>>> This is a nested blockquote

>>>> This is a nested blockquote


Here is a footnote reference,[^1]
[^1]: And here is the footnote.


2^2^2


*[HTML]: Hyper Text Markup Language


==This text is highlighted==


:smile:


This is a citation.[^1]
[^1]: This is a citation.


---


++This text is inserted++


# Heading 1 
## Heading 2 
### Heading 3 
#### Heading 4 
##### Heading 5 
###### Heading 6 


**This text is bold**


<sub>This text is small</sub>


[Google](https://www.google.com)

[facebook](https://www.facebook.com "This is a title")


- [x] This is a complete item
- [ ] This is an incomplete item


--This text is deleted--


<details>
<summary>Click to expand!</summary>
</details>


| Tables | Are | Cool |
| --- | --- | --- |
| col 3 is | right-aligned | $1600 |
| col 2 is | centered | $12 |
| zebra stripes | are neat | $1 |


![This is an image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

![This is an image](https://images.pexels.com/photos/14980905/pexels-photo-14980905.jpeg "This is a title")

![This is an image](https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg)


`This text is code`


<details>
<summary>Click to expand!</summary>
</details>


Term
: Definition


~~This text is strikethrough~~


$$
\begin{align}
\end{align}
$$


*This text is italic*

_This text is italic_
