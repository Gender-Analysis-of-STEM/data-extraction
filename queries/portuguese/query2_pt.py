import twint

c = twint.Config()
c.Since = "2019-02-01"
c.Until = "2019-03-14"
c.Search = '(mulher OR mulheres OR garotinha OR garotas OR menina OR garotas) AND \
    ((engenheira OR cientista OR arquiteta OR programação OR biologa) OR \
    (engenharia OR ciência OR stem)) OR \
    (biologia  OR TIC OR arquitetura)'
c.Lang = "pt"
c.Store_csv = True
c.Output = "./Query2_2019_pt.csv"
twint.run.Search(c)
