
# decorator


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('hi')
# print(print_h1)    #  <function html_tag.<locals>.wrap_text at 0x0167C618>
print_h1('Test Headline!')      # the inner func takes an argument: msg
print_h1('Another Headline!')
print_p = html_tag('p')
print_p('Test Paragraph!')
