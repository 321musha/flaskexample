def searchbyreg(pattern):
    '''выводит совпадения, найденные в тексте'''
    import re
    from pathlib import PurePath
    p=PurePath('onegin.txt')
    di=dict()

    if len(pattern)==0 or pattern[0]==' ':
        return 'Поле пустое'

    with open(p, encoding='utf-8') as fname:
        for line in fname:
            line=line.lower().strip()
            found=re.findall(pattern, line)
            if len(found)>0:
                for one in found:
                    di[one]=di.get(one,0)+1

    if len(di)==0:
        return 'Не найдено. Попробуйте ещё раз.'

    if len(di)!=0:
        return list(di.keys())

    di.clear()
