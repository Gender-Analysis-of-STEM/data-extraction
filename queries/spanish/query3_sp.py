import twint

c = twint.Config()
c.Since = "2019-02-01"
c.Until = "2019-03-14"
c.Search = '(mujer OR mujeres OR niña OR niñas OR chica OR chicas) AND \
((ingeniera OR científica OR arquitecta OR programadora OR bióloga) OR \
(ingeniería OR ciencia OR stem)) OR \
(química OR bioquímica OR ecología OR geología OR astrofísica OR astronomía OR electronica OR \
mécanica OR computación)'
c.Lang = "es"
c.Store_csv = True
c.Output = "./Query3_2021.csv"
twint.run.Search(c)
