page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
# start_link = page.find('<a href=')
# first_quote = page.find('"', start_link + 1)
# end_quote = page.find('"', first_quote + 1)
# url = page[first_quote + 1:end_quote]


def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[first_quote + 1:end_quote]
    return end_quote, url

