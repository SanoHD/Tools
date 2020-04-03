"""
Made by CMinusMinus (SanoHD)
https://github.com/SanoHD
------------------------------------------------------------------------
This is a simple lexer for one line of code. A lexer is used
in programming languages to understand a line of code and cut
it into its pieces. The Lexer returns a list with strings. Each
string has a letter (S,F,I,B,V,X) and a # in front of it. This
letter shows, what the text after it and the # is.

S - String
F - Float
I - Int
B - Bool
V - Variable or keyword
X - Everything Else, things with special characters (+/!/$/...)

A piece of code...

print "Hello World!" 1 testvar
var x = 50
var y = "Long String"

...is cutted like this:

["V#print","S#Hello World!","I#1","V#testvar"]
["V#var","V#x","X#=","I#50"]
["V#var","V#y","X#=","S#Long String"]
"""



def Lexer(y):
    read = False
    end = []
    e = ""
    y += " NONE"
    for x in y:
        e += x
        if read == True and x == '"':
            read = False
            end.append("S#"+e.strip())
            e = ""
        elif read == False and x == '"':
            read = True
        if read == False and x == ' ':
            issymbol = False
            if e.strip() == "": continue
            for E in e.strip():
                if not E in abc: issymbol = True; break
            if issymbol == True:
                if e.strip() != ",": end.append("X#"+e.strip())
            else:
                if "." in e.strip():
                    try:
                        float(e.strip())
                        end.append("F#"+e.strip())
                    except: pass
                else: # NO VARIABLES WITH DOTS ALLOWED!
                    try:
                        int(e.strip())
                        end.append("I#"+e.strip())
                    except:
                        if e.strip() == "false" or e.strip() == "true":
                            end.append("B#"+e.strip())
                        else:
                            end.append("V#"+e.strip())
            e = ""
    END = []
    for e in end:
        if e != "": END.append(e)
    return END

