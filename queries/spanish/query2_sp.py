import twint

c = twint.Config()
c.Since = "2021-02-01"
c.Until = "2021-03-14"
c.Search = "(mujer OR mujeres OR niña OR niñas OR chica OR chicas) AND \
((ingeniera OR científica OR arquitecta OR programadora OR bióloga) OR \
(ingeniería OR ciencia OR stem)) OR \
(biología OR TIC OR arquitectura)"
c.Lang = "es"
c.Store_csv = True
c.Output = "/Users/marianafernandez/Documents/FashionableBID/Gender-Analysis-of-STEM/data-raw/Query2_2021.csv"
twint.run.Search(c)
