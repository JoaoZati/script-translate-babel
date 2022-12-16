from translate import Translator

file_path = "/home/joao/Dev/brain/app/translations/en/LC_MESSAGES/messages_copy.po"


def split_and_append_from_caracter(str_new, str_file, caracter):
    lst_split = str_file.split(caracter)
    str_new += lst_split[0] + caracter
    str_file = caracter.join(lst_split[1:])

    return str_new, str_file


def translate_word_from_old_to_new(str_new, str_file, translator, translate_olds=False):
    """
    str_new: str, string will be created a new file
    str_file: str, string from old po file that will be translated

    return:
    str_new: str, string with translated word in msgstr
    str_file: str, str_file without word translated
    """

    str_new, str_file = split_and_append_from_caracter(str_new, str_file, 'msgid "')

    str_palavra_a_traduzir = str_file.split('"')[0]

    str_new, str_file = split_and_append_from_caracter(str_new, str_file, 'msgstr "')

    lst_traducao = str_file.split('"')
    str_palavra_traduzida = lst_traducao[0]

    if not str_palavra_traduzida or translate_olds:
        str_palavra_traduzida = translator.translate(str_palavra_a_traduzir)

    if len(lst_traducao) <= 2:
        str_new += str_palavra_traduzida + '"'
        return str_new, ""

    str_file = str_palavra_traduzida + '"' + '"'.join(lst_traducao[1:])

    return str_new, str_file


def main():
    to_lang = input("Digite a linguagem para traduzir do portugues (Ex: 'en', 'es'): ")
    translator = Translator(to_lang=to_lang, from_lang='pt')

    with open(file_path, 'r') as file:
        str_file = file.read()

    # Coping init of file_string in a new string with caracter '#:'
    str_new, str_file = split_and_append_from_caracter('', str_file, '#:')
    while True:
        str_new, str_file = translate_word_from_old_to_new(str_new, str_file, translator)
        if not str_file:
            break

    with open('messages.po', 'w') as text_file:
        text_file.write(str_new)


if __name__=='__main__':
    main()
