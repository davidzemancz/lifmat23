import APIPrompt

def get_chapters(message):
    prompt = "Jakých z následujícíh oblastí se týká následující dotaz? Můžeš vrátit víc oblastí. Vrať výsledek jako indexy odělené čárkou. Oblasti: " + APIPrompt.kapitoly_str + "Dotaz: " + message
    res = APIPrompt.respond4(prompt)
    return list(map(int,res.split(",")))