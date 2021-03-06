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
    return

def job_done(choice):
    easygui.textbox(text = choice + " completed.")
    return

def pdfy(book_name):
    #Insert code to convert images to PDF here.
    os.system('scp uk@192.168.1.102:~/img/*.jpg ~/img/')
    os.system('ssh uk@192.168.1.102 \'rm -rf ~/img/*.jpg\'')

    os.system(r'ls ~/img/*.jpg | sort -n | tr \'\n\' \' \' | sed \'s/$/\ ~/%s.pdf/\' | xargs convert' % (book_name))
    os.system('rm -rf ~/img/*.jpg')
    print("something related to PDFs")
    return

def textify(book_name, num_pages):
    #Insert code to convert images to text here.
    for i in range(num_pages):
        if i % 2 == 0:
            os.system('tesseract ~/img/%d.jpg ~/img/%d.txt' % (i, i))
        else:
            os.system('ssh uk@192.168.1.102 \'tesseract ~/img/%d.jpg ~/img/%d.txt\'' % (i, i))

    os.system('scp uk@192.168.1.102 ~/img/*.txt ~/img/')
    os.system('ssh uk@192.168.1.102 \'rm -rf ~/img/*.txt\'')

    for i in range(num_pages):
        os.system('cat ~/img/%d.txt >> ~/%s.txt' % (i, book_name))

    print("something related to text")
    return

def translate_regions(choice):
    title = "Select Language for translation"
    if choice == "Indian Languages":
        msg = "Choose any following Indian Language for translation : "
        choices = ["Bengali", "English", "Gujarati", "Hindi", "Kannada", "Malayalam", "Marathi", "Punjabi", "Sindhi", "Tamil", "Telugu", "Urdu"]
        lang_choice = easygui.choicebox(msg, title, choices)
        return lang_choice
    else:
        msg = "Choose any following Foreign Language for translation : "
        choices = ["Afrikaans", "Amharic", "Arabic", "Azerbaijani", "Belarusian", "Bulgarian", "Bosnian", "Catalan", "Cebuano", "Corsican", "Czech", "Welsh", "Danish", "German", "Greek", "English", "Esperanto", "Spanish", "Estonian", "Basque", "Persian", "Finnish", "Fijian", "French", "Frisian", "Irish", "Scots Gaelic", "Galician", "Hausa", "Hawaiian", "Hebrew", "Hmong", "Croatian", "Haitian Creole", "Hungarian", "Armenian", "Indonesian", "Igbo", "Icelandic", "Italian", "Japanese", "Javanese", "Georgian", "Kazakh", "Khmer", "Korean", "Kurdish", "Kyrgyz", "Latin", "Luxembourgish", "Lao", "Lithuanian", "Latvian", "Malagasy", "Maori", "Macedonian", "Mongolian", "Malay", "Maltese", "Hmong Daw", "Myanmar", "Nepali", "Dutch", "Norwegian", "Chichewa", "Queretaro Otomi", "Polish", "Pashto", "Portuguese", "Romanian", "Russian", "Sinhala", "Slovak", "Slovenian", "Samoan", "Shona", "Somali", "Albanian", "Sesotho", "Sundanese", "Swedish", "Swahili", "Tajik", "Thai", "Filipino", "Klingon", "Tongan", "Turkish", "Tatar", "Tahitian", "Udmurt", "Ukrainian", "Uzbek", "Vietnamese", "Xhosa", "Yiddish", "Yoruba", "Yucatec Maya", "Cantonese", "Chinese Simplified", "Chinese Traditional", "Zulu"]
        lang_choice = easygui.choicebox(msg, title, choices)
        return lang_choice

def translate(book_name):
    #Insert code to translate text here.
    title = "Select Language for translation"
    msg = "Choose any region for the language selection."
    choices = ["Foreign Languages", "Indian Languages"]
    choice = easygui.choicebox(msg, title, choices)
    lang = translate_regions(choice)

    lang_dict = {
            "Afrikaans" : "af",
            "Amharic" : "am",
            "Arabic" : "ar",
            "Azerbaijani" : "az",
            "Belarusian" : "be",
            "Bulgarian" : "bg",
            "Bengali" : "bn",
            "Bosnian" : "bs",
            "Catalan" : "ca",
            "Cebuano" : "ceb",
            "Corsican" : "co",
            "Czech" : "cs",
            "Welsh" : "cy",
            "Danish" : "da",
            "German" : "de",
            "Greek" : "el",
            "English" : "en",
            "Esperanto" : "eo",
            "Spanish" : "es",
            "Estonian" : "et",
            "Basque" : "eu",
            "Persian" : "fa",
            "Finnish" : "fi",
            "Fijian" : "fj",
            "French" : "fr",
            "Frisian" : "fy",
            "Irish" : "ga",
            "Scots Gaelic" : "gd",
            "Galician" : "gl",
            "Gujarati" : "gu",
            "Hausa" : "ha",
            "Hawaiian" : "haw",
            "Hebrew" : "he",
            "Hindi" : "hi",
            "Hmong" : "hmn",
            "Croatian" : "hr",
            "Haitian Creole" : "ht",
            "Hungarian" : "hu",
            "Armenian" : "hy",
            "Indonesian" : "id",
            "Igbo" : "ig",
            "Icelandic" : "is",
            "Italian" : "it",
            "Japanese" : "ja",
            "Javanese" : "jv",
            "Georgian" : "ka",
            "Kazakh" : "kk",
            "Khmer" : "km",
            "Kannada" : "kn",
            "Korean" : "ko",
            "Kurdish" : "ku",
           "Kyrgyz" : "ky",
           "Latin" : "la",
           "Luxembourgish" : "lb",
           "Lao" : "lo",
           "Lithuanian" : "lt",
           "Latvian" : "lv",
           "Malagasy" : "mg",
           "Maori" : "mi",
           "Macedonian" : "mk",
           "Malayalam" : "ml",
           "Mongolian" : "mn",
           "Marathi" : "mr",
           "Malay" : "ms",
           "Maltese" : "mt",
           "Hmong Daw" : "mww",
           "Myanmar" : "my",
           "Nepali" : "ne",
           "Dutch" : "nl",
           "Norwegian" : "no",
           "Chichewa" : "ny",
           "Queretaro Otomi" : "otq",
           "Punjabi" : "pa",
           "Polish" : "pl",
           "Pashto" : "ps",
           "Portuguese" : "pt",
           "Romanian" : "ro",
           "Russian" : "ru",
           "Sindhi" : "sd",
           "Sinhala" : "si",
           "Slovak" : "sk",
           "Slovenian" : "sl",
           "Samoan" : "sm",
           "Shona" : "sn",
           "Somali" : "so",
           "Albanian" : "sq",
           "Serbian (Cyrillic)" : "sr-Cyrl",
           "Serbian (Latin)" : "sr-Latn",
           "Sesotho" : "st",
           "Sundanese" : "su",
           "Swedish" : "sv",
           "Swahili" : "sw",
           "Tamil" : "ta",
           "Telugu" : "te",
           "Tajik" : "tg",
           "Thai" : "th",
           "Filipino" : "tl",
           "Klingon" : "tlh",
           "Klingon (plqaD)" : "tlh-Qaak",
           "Tongan" : "to",
           "Turkish" : "tr",
           "Tatar" : "tt",
           "Tahitian" : "ty",
           "Udmurt" : "udm",
           "Ukrainian" : "uk",
           "Urdu" : "ur",
           "Uzbek" : "uz",
           "Vietnamese" : "vi",
           "Xhosa" : "xh",
           "Yiddish" : "yi",
           "Yoruba" : "yo",
           "Yucatec Maya" : "yua",
           "Cantonese" : "yue",
           "Chinese Simplified" : "zh-CN",
           "Chinese Traditional" : "zh-TW",
           "Zulu" : "zu"
    }
    easygui.msgbox("Translating to " + lang + " language...")
    os.system('~/ira-book-scanner/translator/translate-shell -b -i ~/%s.txt en: :%s -o ~/%s_%s.txt' % (book_name, lang_dict[lang], book_name, lang_dict[lang]))
    easygui.msgbox("Translation completed.", "Done")
    # print("something related to translate")
    return

def audiofy(book_name):
    #Insert code to convert text to mp3 here.
    msg = "Choose any following language for an audio format : "
    title = "Select Language for audio"
    choices = ["English - GB (default)", "English - US", "German", "Spanish", "French", "Italian"]
    choice = easygui.choicebox(msg, title, choices)
    easygui.msgbox("Generating audio file in " + choice + " language...")
    easygui.msgbox("Audio file generated.", "Done")

    lang_dict = {
            'English - GB (default)' : 'en-GB',
            'English - US' : 'en-US',
            'German' : 'de-DE',
            'Spanish' : 'es-ES',
            'French' : 'fr-FR',
            'Italian' : 'it-IT'
            }

    os.system('~/ira-book-scanner/txt2wave/txt2wave.py -i ~/%s.txt -l %s' % (book_name, lang_dict[choice]))
    # print("something related to audio")
    return

def snap(num_pages):
    os.system('~/ira-book-scanner/pi-snapper/snap %d' % (num_pages))
    return

def image_process(num_pages):
    os.system('mogrify -colorspace GRAY ~/img/*.*')

    for i in range(num_pages):
        if i % 2 == 0:
            os.system('~/ira-book-scanner/dp_easygui/textcleaner ~/img/%d.jpg ~/img/%d.jpg' % (i, i))
        else:
            os.system('ssh uk@192.168.1.102 \'~/ira-book-scanner/dp_easygui/textcleaner ~/img/%d.jpg ~/img/%d.jpg\'' % (i, i))

    return

def main():

    book_name = easygui.enterbox("Enter Book Name", "Book Name")
    if book_name == "":
        easygui.msgbox("No book name given.", "Error")
        exit()

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

    given_choices, selected_choices = select_choice(book_name)

    os.system('ssh uk@192.168.1.2 \'cd arduino/ira/ && ino build && ino upload && cd\'')
    snap(book_pages)

    image_process(book_pages)

    textify(book_name, book_pages)

    if "PDF" in selected_choices:
        pdfy(book_name)

    if "Translation" in selected_choices:
        translate(book_name)

    if "Audio Generation" in selected_choices:
        audiofy(book_name)

    # if selected_choices:
    #     for choice in selected_choices:
    #         job_in_progress(choice)
    #         #Insert job function call here.
    #         job_done(choice)
    # else:
    #     exit()

main()
