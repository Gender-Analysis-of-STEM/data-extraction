import twint

c = twint.Config()
c.Since = "2019-02-01"
c.Until = "2019-03-14"
c.Search = "(mujer OR mujeres OR niña OR niñas OR chica OR chicas) AND \
((ingeniera OR científica OR arquitecta OR programadora OR bióloga) OR \
(ingeniería OR ciencia OR stem)) OR \
(tecnología  OR software OR metalurgía OR minería OR agronomía OR automotriz)"
c.Lang = "es"
c.Store_csv = True
c.Output = "./Query3.2_2019.csv"
twint.run.Search(c)
