import mistune

#using mistune compliing with cython

def MD_parser(text):
    
    MD_form = mistune.markdown(text)
    return MD_form

input_user = raw_input("input any text you want: ")
text = input_user

print MD_parser(text) 

#if input text is: I am so so sick, **and it kills me**
#output: <p>I am so so sick, <strong>and it kills me</strong></p>