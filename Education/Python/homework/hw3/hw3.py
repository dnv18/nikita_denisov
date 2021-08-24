def input_max_len():
    x = int(input('Input line max len (>35): '))
    if x < 35:
        input_max_len()
    else:
        return x


def format_txt(txt, max_len):
    format_text = ''
    for line in txt.split('\n'):
        whitespaces_add = max_len - len(line)
        line_list = line.split(' ')
        if len(line_list) > 1:
            while whitespaces_add > 0:
                for i in range(len(line_list)-1):
                    if whitespaces_add > 0:
                        line_list[i] += ' '
                        whitespaces_add -= 1
                    else:
                        format_text += ' '.join(line_list) + '\n'
                        break
        else:
            format_text += ' '.join(line_list) + '\n'
    return format_text


def create_format_txt(file):
    with open(file, 'r+') as rf:
        max_len = input_max_len()
        new_text = ''
        c = 0
        for i in rf.read().split():
            c += len(i)
            if c >= max_len:
                new_text += '\n'
                c = len(i)
            elif new_text != '':
                new_text += ' '
                c += 1
            new_text += i
        format_text = format_txt(new_text, max_len)
    with open('new_text.txt', 'w') as writer:
        writer.write(format_text)
    print('Done.')


create_format_txt('text.txt')
