# def trans(text):
text_spanish = "je très intéressé laprogrammation".rsplit()
text_persian = "man kheili alaghemand barnamenevisiam".rsplit()
text_english = "i very interested programming".rsplit()


def trans(text, text2):
    for num in range(4):
        replacer = text[num].replace(text[num], text2[num])
        print(replacer)


trans(text_persian, text_english)
