import twint

c = twint.Config()
c.Since = "2021-02-01"
c.Until = "2021-03-14"
c.Search = "(mujer OR mujeres OR niña OR niñas OR chica OR chicas) AND \
    ((ingeniera OR científica OR arquitecta OR programadora OR bióloga) OR \
    (ingeniería OR ciencia OR stem)) OR \
    (matemáticas) OR \
    (#WomenInSTEM OR #WomenInTech OR #MujeresEnTI OR #MujeresEnIT OR #GirlsInTech)"
c.Lang = "es"
c.Store_csv = True
c.Output = "./Query1_2021.csv"
twint.run.Search(c)
