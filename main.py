from translate import Translator

def split_and_append_from_caracter(str_new, str_file, caracter):
    lst_split = str_file.split(caracter)
    str_new += lst_split[0] + caracter
    str_file = caracter.join(lst_split[1:])

    return str_new, str_file


def split_translate_and_append_word(
    str_new, str_file, str_palavra_a_traduzir, translator, translate_olds, number_print
):
    """

    Return:
    str_new: palavra terminando com 
    """

    lst_traducao = str_file.split('"\n\n')
    str_palavra_traduzida = lst_traducao[0] + '"\n\n'

    palavra_traducao = 'Traducão Pulada'
    if str_palavra_traduzida in ["", '"\n', '"\n\n'] or translate_olds:
        str_palavra_traduzida = translator.translate(
            str_palavra_a_traduzir.replace('"', '\"').replace('\n', '\\n')
        ) + "\\n"
        str_palavra_traduzida = str_palavra_traduzida.replace('\\n', '\n')
        palavra_traducao = 'Traduzido'

    print(
        f'{number_print}) {palavra_traducao}:|{str_palavra_a_traduzir}| - Para:|{str_palavra_traduzida}|'
    )

    if len(lst_traducao) < 2:
        str_new += str_palavra_traduzida
        return str_new, ""

    str_file = str_palavra_traduzida + '"\n\n'.join(lst_traducao[1:])

    return str_new, str_file


def translate_word_from_old_to_new(
    str_new,
    str_file,
    translator,
    translate_olds=False,
    number_print=1,
):
    """
    str_new: str, string will be created a new file
    str_file: str, string from old po file that will be translated

    return:
    str_new: str, string with translated word in msgstr
    str_file: str, str_file without word translated
    """

    str_new, str_file = split_and_append_from_caracter(str_new, str_file, 'msgid "')

    str_palavra_a_traduzir = str_file.split('msgstr "')[0]

    str_new, str_file = split_and_append_from_caracter(str_new, str_file, 'msgstr "')

    return split_translate_and_append_word(
        str_new, str_file, str_palavra_a_traduzir, translator, translate_olds, number_print
    )


def generate_message_po(file_path, file_path_out, to_lang, from_lang='pt', translate_olds=False):
    translator = Translator(to_lang=to_lang, from_lang=from_lang)

    with open(file_path, 'r') as file:
        str_file = file.read()

    # Coping init of file_string in a new string with caracter '#:' (to jump first msgid)
    str_new, str_file = split_and_append_from_caracter('', str_file, '#:')
    count = 0
    while True:
        count += 1
        str_new, str_file = translate_word_from_old_to_new(
            str_new, str_file, translator, translate_olds, number_print=count
        )

        if not str_file:
            break

    with open(file_path_out, 'w') as text_file:
        text_file.write(str_new)


if __name__=='__main__':
    file_path_en = "/home/joaozati/Dev/brain/app/translations/en/LC_MESSAGES/messages.po"
    file_path_out_en = "/home/joaozati/Dev/brain/app/translations/en/LC_MESSAGES/messages_en.po"
    file_path_es = "/home/joaozati/Dev/brain/app/translations/es/LC_MESSAGES/messages.po"
    file_path_out_es = "/home/joaozati/Dev/brain/app/translations/es/LC_MESSAGES/messages_es.po"

    print('#'*100)
    print('Traduzindo messages_en.po')
    generate_message_po(file_path_en, file_path_out_en, 'en', from_lang='pt')
    # print('#'*100)
    # print('Traduzindo messages_es.po')
    # generate_message_po(file_path_es, file_path_out_es, 'es', from_lang='pt')
