import random
import datetime
import os


class Content:

    def generateMarkdown(self, title, sequence, type, section):

        # Front Matter

        frontMatter = self.frontMatter(title, sequence, type, section)

        # Grey Matter

        greyMatter = self.greyMatter()

        # Markdown

        # Content

        content = frontMatter + greyMatter
        return content

    def frontMatter(self, title, sequence, type, section):

        content = "---\n"
        if type == 'course':
            content += "lastmod: " + str(datetime.datetime.now()) + "\n"
            content += "title: " + title + "\n"
            content += "description: " + title + "\n"
            content += "weight: " + str(random.randint(1, 100)) + "\n"
            content += "emogi: " + ["🤭", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐",
                                    "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑"][random.randint(0, 32)] + "\n"
            content += "type: " + type + "\n"
            content += "author : Akash Aman\n"

        elif type == 'chapter':
            content += "title: " + title + "\n"
            content += "description: " + title + "\n"
            content += "weight: " + str(random.randint(1, 100)) + "\n"
            content += "emogi: " + ["🤭", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐",
                                    "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑"][random.randint(0, 32)] + "\n"
            content += "type: chapters\n"
            content += "chapter: " + str(sequence) + "\n"

        if section != "":
            content += "section_start: " + section + "\n"
            content += "section_emogi: " + ["🤭", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐",
                                            "🤢", "🤧", "🤮", "🤕", "🤑", "🤠", "🤡", "🤥", "🤫", "🤔", "🤐", "🤢", "🤧", "🤮", "🤕", "🤑"][random.randint(0, 32)] + "\n"
        content += "---\n"
        return content

    def greyMatter(self):
        return (Markdown()).getMarkdown()

    def create(self, courseCount ,chapterCount):

        for i in range(courseCount):
            course = self.generateMarkdown("Course " + str(i + 1), i + 1, 'course', "")
            ## Create Course Directory recursive.
            os.makedirs("courses/course-" + str(i + 1))
            with open("courses/course-" + str(i + 1) + "/_index.md", "w", encoding="utf-8") as file:
                file.write(course)
                file.close()

            count = 0
            for j in range(chapterCount):
                
                section = ""
                if count == 0 or random.randint(0, 6) == 3:
                    count += 1
                    section = "Section " + str(count)

                chapter = self.generateMarkdown("Chapter " + str(j + 1), j + 1, 'chapter', section)
                with open("courses/course-" + str(i + 1) + "/chapter-" + str(j + 1) + ".md", "w", encoding="utf-8") as file:
                    file.write(chapter)
                    file.close()    
            
        return True
    

class Markdown:

    def __init__(self):

        self.functions = [

            self.headings,

            self.bold,

            self.italic,

            self.code,

            self.links,

            self.images,

            self.blockquotes,

            self.lists,

            self.horizontalRule,

            self.tables,

            self.strikethrough,

            self.taskLists,

            self.emogi,

            self.math,

            self.superscript,

            self.subscript,

            self.footnotes,

            self.definitionLists,

            self.abbreviations,

            self.citations,

            self.insertions,

            self.deletions,

            self.details,

            self.summary,

            self.mark,

            self.small,

            self.time

        ]

    def getMarkdown(self):

        markdown = ''

        count = len(self.functions)

        for i in range(count):

            index = random.randint(0, len(self.functions) - 1)

            markdown += "\n" + self.functions[index]()

            self.functions.pop(index)

        return markdown

    def headings(self):

        heading = '\n# Heading 1 \n'

        heading += '## Heading 2 \n'

        heading += '### Heading 3 \n'

        heading += '#### Heading 4 \n'

        heading += '##### Heading 5 \n'

        heading += '###### Heading 6 \n'

        return heading

    def bold(self):

        bold = '\n**This text is bold**\n'

        return bold

    def italic(self):

        italic = '\n*This text is italic*\n'

        italic += '\n_This text is italic_\n'
        return italic

    def code(self):

        code = '\n`This text is code`\n'
        return code

    def links(self):

        links = '\n[Google](https://www.google.com)\n'

        links += '\n[facebook](https://www.facebook.com "This is a title")\n'

        return links

    def images(self):

        images = '\n![This is an image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)\n'

        images += '\n![This is an image](https://images.pexels.com/photos/14980905/pexels-photo-14980905.jpeg "This is a title")\n'

        images += '\n![This is an image](https://images.pexels.com/photos/1612351/pexels-photo-1612351.jpeg)\n'

        return images

    def blockquotes(self):

        blockquotes = '\n> This is a blockquote\n'

        blockquotes += '\n> Quote: facts doesn`t cares feelings \n'

        blockquotes += '\n> This is a nested blockquote\n'

        blockquotes += '\n>> This is a nested blockquote\n'

        blockquotes += '\n>>> This is a nested blockquote\n'

        blockquotes += '\n>>>> This is a nested blockquote\n'

        return blockquotes

    def lists(self):

        lists = '\n1. This is a numbered list\n'

        lists += '2. This is a numbered list\n'

        lists += '3. This is a numbered list\n'

        lists += '4. This is a numbered list\n'

        lists += '- This is a list\n'

        lists += '- This is a nested list\n'

        lists += '\t- This is a nested list\n'

        lists += '\t\t- This is a nested list\n'

        lists += '\t\t\t- This is a nested list\n'

        lists += '\t\t\t\t- This is a nested list\n'
        return lists

    def horizontalRule(self):

        horizontalRule = '\n---\n'

        return horizontalRule

    def tables(self):

        tables = '\n| Tables | Are | Cool |\n'

        tables += '| --- | --- | --- |\n'

        tables += '| col 3 is | right-aligned | $1600 |\n'

        tables += '| col 2 is | centered | $12 |\n'

        tables += '| zebra stripes | are neat | $1 |\n'

        return tables

    def strikethrough(self):

        strikethrough = '\n~~This text is strikethrough~~\n'

        return strikethrough

    def taskLists(self):

        taskLists = '\n- [x] This is a complete item\n'

        taskLists += '- [ ] This is an incomplete item\n'

        return taskLists

    def emogi(self):

        emogi = '\n:smile:\n'

        return emogi

    def math(self):

        math = '\n$$\n'

        math += '\\begin{align}\n'

        math += '\\end{align}\n'

        math += '$$\n'
        return math

    def superscript(self):

        superscript = '\n2^2^2\n'

        return superscript

    def subscript(self):

        subscript = '\nH~2~O\n'

        return subscript

    def footnotes(self):

        footnotes = '\nHere is a footnote reference,[^1]\n'

        footnotes += '[^1]: And here is the footnote.\n'
        return footnotes

    def definitionLists(self):

        definitionLists = '\nTerm\n'

        definitionLists += ': Definition\n'

        return definitionLists

    def abbreviations(self):

        abbreviations = '\n*[HTML]: Hyper Text Markup Language\n'

        return abbreviations

    def citations(self):

        citations = '\nThis is a citation.[^1]\n'

        citations += '[^1]: This is a citation.\n'
        return citations

    def insertions(self):

        insertions = '\n++This text is inserted++\n'
        return insertions

    def deletions(self):

        deletions = '\n--This text is deleted--\n'
        return deletions

    def details(self):

        details = '\n<details>\n'

        details += '<summary>Click to expand!</summary>\n'

        details += '</details>\n'
        return details

    def summary(self):

        summary = '\n<details>\n'

        summary += '<summary>Click to expand!</summary>\n'


        summary += '</details>\n'

        return summary

    def mark(self):

        mark = '\n==This text is highlighted==\n'

        return mark

    def small(self):

        small = '\n<sub>This text is small</sub>\n'
        return small

    def time(self):

        time = '\n<time datetime="2013-04-06T12:32+00:00">2 weeks ago</time>\n'
        return time




# convert add_numbers() to static method

print((Content()).create(5,20) )
