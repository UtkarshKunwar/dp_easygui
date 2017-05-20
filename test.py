import easygui
import os
import sys

def select_choice(name):
    msg = "Reading book \"" + name + "\". Choose the output formats"
    title = "Output Formats"
    choices = ["Text Generation", "Translation", "Audio Generation", "PDF Generation"]
    choice = easygui.multchoicebox(msg, title, choices)
    return choices, choice

def job_in_progress(choice):
    text = choice + " in progress..."
    easygui.textbox(text = text)

def job_done(choice):
    easygui.textbox(text = choice + " completed.")

def pdfy():
    #Insert code to convert images to PDF here.
    print("something related to PDFs")

def textify():
    #Insert code to convert images to text here.
    print("something related to text")

def translate_regions(choice):
    title = "Select Language for translation"
    if choice == "Indian Languages":
        msg = "Choose any following Indian Language for translation : "
        choices = ["Bengali", "English", "Gujarati", "Hindi", "Kannada", "Malayalam", "Marathi", "Punjabi", "Sindhi", "Tamil", "Telugu"]
        lang_choice = easygui.choicebox(msg, title, choices)
        return lang_choice
    else:
        msg = "Choose any following Indian Language for translation : "
        choices = ["German", "French", "Italian"]
        lang_choice = easygui.choicebox(msg, title, choices)
        return lang_choice

def translate():
    #Insert code to translate text here.
    title = "Select Language for translation"
    msg = "Choose any region for the language selection."
    choices = ["Foreign Languages", "Indian Languages"]
    choice = easygui.choicebox(msg, title, choices)
    lang = translate_regions(choice)
    easygui.msgbox("Translating to " + lang + " language...")
    easygui.msgbox("Translation completed.", "Done")
    return
    # print("something related to translate")

def audiofy():
    #Insert code to convert text to mp3 here.
    msg = "Choose any following language for an audio format : "
    title = "Select Language for audio"
    choices = ["English - GB (default)", "English - US", "German", "Spanish", "French", "Italian"]
    choice = easygui.choicebox(msg, title, choices)
    easygui.msgbox("Generating audio file in " + choice + " language...")
    easygui.msgbox("Audio file generated.", "Done")
    # print("something related to audio")
    return

def snap(num_pages):
    os.system('../pi-snapper/snap %d' % (num_pages))
    return

def main():

    book_name = easygui.enterbox("Enter Book Name", "Book Name")
    if book_name == "":
        easygui.msgbox("No book name given.", "Error")
        exit()
    given_choices, selected_choices = select_choice(book_name)

    book_pages=-1
    while True:
        book_pages = easygui.enterbox("Enter the number of pages", "Pages")
        try:
            book_pages = int(book_pages)
        except ValueError:
            easygui.msgbox("Number of pages must be an integer.", "Error")
            continue
        else:
            break

    snap(book_pages)

    textify()

    if "Translation" in selected_choices:
        translate()

    if "Audio Generation" in selected_choices:
        audiofy()

    if "PDF" in selected_choices:
        pdfy()

    # if selected_choices:
    #     for choice in selected_choices:
    #         job_in_progress(choice)
    #         #Insert job function call here.
    #         job_done(choice)
    # else:
    #     exit()

main()
