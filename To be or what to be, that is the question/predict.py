# Ranked #1 in Hackerrank 'To be or what to be, that is the question' question.
to_be = ['am', 'is', 'are', 'was', 'were', 'been', 'being', 'be']
to_be_be = ['will', 'would', 'can', 'could', 'shall', 'should', 'must', 'might', 'may', 'will', 'won\'t', 'wouldn\'t', 'can\'t', 'couldn\'t', 'shan\'t', 'shouldn\'t', 'mustn\'t']
to_be_been = ['has', 'have', 'had', 'hasn\'t', 'haven\'t', 'hadn\'t']
to_be_being = ['is', 'are', 'was', 'were', 'isn\'t', 'aren\'t', 'wasn\'t', 'weren\'t']
plural = ['they', 'we', 'you', 'They', 'We', 'You']


def answer(words_list):
    for i, word in enumerate(words_list):
        if word == '----' or word == '----.':
            prev = words_list[i - 1]
            _next = words_list[i + 1]

            if prev == 'i':
                print('am')
                continue

            if prev in to_be_be or words_list[i - 2] in to_be_be:
                print('be')
                continue

            if prev in to_be_been or words_list[i - 2] in to_be_been:
                print('been')
                continue

            if prev in to_be_being or words_list[i - 2] in to_be_being or prev.endswith('ght'):
                print('being')
                continue

            if _next.endswith('ed') or prev.endswith('ed'):
                if any(map(lambda x: x.endswith('s') and not x.endswith('ss'), words_list[i - 5:i + 5])):
                    print('were')
                    continue
                else:
                    print('was')
                    continue

            if prev.endswith('s') and not prev.endswith('ss'):
                print('were')
                continue

            if _next == 'won':
                print('was')
                continue

            if _next.endswith('ing'):
                if any(map(lambda x: x.endswith('ed'), words_list[i - 20:i + 5])):
                    if (prev.endswith('s') and not prev.endswith('ss')) or prev in plural:
                        print('were')
                        continue
                    else:
                        print('was')
                        continue
                else:
                    if (prev.endswith('s') and not prev.endswith('ss')) or prev in plural:
                        print('are')
                        continue
                    else:
                        print('is')
                        continue

            if not _next.endswith('ing') and not _next.endswith('ed'):
                if any(map(lambda x: x.endswith('ed'), words_list[i - 5:i + 5])):
                    if prev.endswith('s') and not prev.endswith('ss'):
                        print('were')
                        continue
                    else:
                        print('was')
                        continue
                else:
                    if prev.endswith('s') and not prev.endswith('ss'):
                        print('are')
                        continue
                    else:
                        print('is')
                        continue


if __name__ == '__main__':
    blanks = int(input())
    text = input()

    words_list = text.lower().strip().split(' ')
    answer(words_list)
