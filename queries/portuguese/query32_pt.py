import twint

c = twint.Config()
c.Since = "2021-02-01"
c.Until = "2021-03-14"
c.Search = '(mulher OR mulheres OR garotinha OR garotas OR menina OR garotas) AND \
        ((engenheira OR cientista OR arquiteta OR programação OR biologa) OR \
        (engenharia OR ciência OR stem)) OR \
        (tecnología OR software OR aeronáutica OR aeronaval OR \
        OR metais OR mining OR agronomia OR automóvel)'
c.Lang = "pt"
c.Store_csv = True
c.Output = "./Query3.2_2021_pt.csv"
twint.run.Search(c)
