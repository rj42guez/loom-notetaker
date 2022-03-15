def process_bold_italics(candidate):
    # markdown formatting is as follows: 
    # **bold**
    # *italics*

    # we need to figure out how to do this:
    # **bold** -> [b]bold[/b]
    # *italics* -> [i]italics[/i]

    # candidate is a string

    # regex to detect bold is /(\*\*|__)(.*?)\1/
    # regex to detect italix is /(\*|_)(.*?)\1/
