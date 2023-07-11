corner_cases_expressions = [
    "? 0 12 * * /user",
    "-1 0 12 * * /user",
    "60 0 12 * * /user",
    "0-60 0 12 * * /user",
    "0-* 0 12 * * /user",
    "*-0 0 12 * * /user",
    "*-* 0 12 * * /user",
    "*,1 0 12 * * /user",
    "*,* 0 12 * * /user",
    "1,* 0 12 * * /user",
    "*/* 0 12 * * /user",
    "1/* 0 12 * * /user"
]