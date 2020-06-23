from fuzzywuzzy import fuzz
from os import listdir, makedirs
from os.path import isfile, join, sep, getsize, exists
from tqdm import tqdm
import re
import itertools

DIR_ISMDB = join("scripts", "ismdb")
DIR_DAILY = join("scripts", "dailyscript")
DIR_WEEKLY = join("scripts", "weeklyscript")
DIR_SCREEN = join("scripts", "screenplays")
DIR_AWESOME = join("scripts", "awesomefilm")
DIR_SAVANT = join("scripts", "scriptsavant")
DIR_SFY = join("scripts", "sfy")

DIR_FILTER = join("scripts", "filtered")
DIR_FINAL = join("scripts", "final")

ismdb = [join(DIR_ISMDB, f) for f in listdir(DIR_ISMDB) if isfile(
    join(DIR_ISMDB, f)) and getsize(join(DIR_ISMDB, f)) > 3000]
daily = [join(DIR_DAILY, f) for f in listdir(DIR_DAILY) if isfile(
    join(DIR_DAILY, f))and getsize(join(DIR_DAILY, f)) > 3000]
weekly = [join(DIR_WEEKLY, f) for f in listdir(DIR_WEEKLY) if isfile(
    join(DIR_WEEKLY, f))and getsize(join(DIR_WEEKLY, f)) > 3000]
screen = [join(DIR_SCREEN, f) for f in listdir(DIR_SCREEN) if isfile(
    join(DIR_SCREEN, f))and getsize(join(DIR_SCREEN, f)) > 3000]
awesome = [join(DIR_AWESOME, f) for f in listdir(DIR_AWESOME) if isfile(
    join(DIR_AWESOME, f))and getsize(join(DIR_AWESOME, f)) > 3000]
savant = [join(DIR_SAVANT, f) for f in listdir(DIR_SAVANT) if isfile(
    join(DIR_SAVANT, f))and getsize(join(DIR_SAVANT, f)) > 3000]
sfy = [join(DIR_SFY, f) for f in listdir(DIR_SFY) if isfile(
    join(DIR_SFY, f))and getsize(join(DIR_SFY, f)) > 3000]

sources = {
    'ismdb': ismdb,
    'daily': daily,
    'weekly': weekly,
    'screen': screen,
    'awesome': awesome,
    'savant': savant,
    'sfy': sfy
}


def remove_duplicates(arr, comb):

    for (x, y) in tqdm(comb):
        x = x.split('.txt')[0]
        y = y.split('.txt')[0]
        # if x == y:
        #     continue
        result = fuzz.ratio("".join(x.split(sep)[-1].split("-")).lower(),
                            "".join(y.split(sep)[-1].split("-")).lower())
        if result > 98:
            f1 = open( x + '.txt', 'r', errors="ignore")
            file_1 = f1.read()
            f1.close()
            f2 = open( y + '.txt', 'r', errors="ignore")
            file_2 = f2.read()
            f2.close()

            try: 
                if len(file_2.strip()) > len(file_1.strip()):
                    arr.remove(x + '.txt')
                else:
                    arr.remove(y + '.txt')
            except:
                pass

    return arr

for key in sources:
    arr = sources[key]
    print("Remove duplicates from", key, len(arr))
    comb = list(itertools.combinations(arr, 2))
    arr = remove_duplicates(arr, comb)
    print("Non duplicates", len(arr))
    print()


# print("Remove duplicates between sources")
# all_sources = ismdb + daily
# print(len(all_sources))
# comb_all = list(itertools.combinations(all_sources, 2))
# all_sources = remove_duplicates(all_sources, comb_all)
# # print(len(all_sources))
# print()

# all_sources += savant
# print(len(all_sources))
# comb_all = list(itertools.combinations(all_sources, 2))
# all_sources = remove_duplicates(all_sources, comb_all)
# # print(len(all_sources))
# print()

# all_sources += weekly
# print(len(all_sources))
# comb_all = list(itertools.combinations(all_sources, 2))
# all_sources = remove_duplicates(all_sources, comb_all)
# # print(len(all_sources))
# print()

# all_sources += screen
# print(len(all_sources))
# comb_all = list(itertools.combinations(all_sources, 2))
# all_sources = remove_duplicates(all_sources, comb_all)
# # print(len(all_sources))
# print()

# all_sources += awesome
# print(len(all_sources))
# comb_all = list(itertools.combinations(all_sources, 2))
# all_sources = remove_duplicates(all_sources, comb_all)
# print(len(all_sources))

# # print(sorted([x.split(sep)[-1] for x in daily if x not in all_sources]))
# # print(sorted([x.split(sep)[-1] for x in all_sources]))

# # unfiltered = ismdb + daily + weekly


# if not exists(DIR_FILTER):
#     makedirs(DIR_FILTER)


# print("Write cleaned files to new dir")
# for source in tqdm(all_sources):
#     f = open(source, 'r', errors="ignore")
#     data = f.read().strip()
#     f.close()

#     with open(join(DIR_FILTER, source.split(sep)[-1]), 'w', errors="ignore") as out:
#         out.write(data)


# print("Remove different versions of scripts with same name")
# filtered = [join(DIR_FILTER, f) for f in listdir(DIR_FILTER)
#             if isfile(join(DIR_FILTER, f)) and getsize(join(DIR_FILTER, f)) > 3000]
# print(len(filtered))
# comb_filter = list(itertools.combinations(filtered, 2))

# for (x, y) in tqdm(comb_filter):
#     result = fuzz.partial_ratio("".join(x.split(sep)[-1].split('.txt')[0].split("-")).lower(),
#                         "".join(y.split(sep)[-1].split('.txt')[0].split("-")).lower())
#     if result > 60:
#         f1 = open(x, 'r', errors="ignore")
#         file_1 = f1.read().replace("\n", " ").replace("\t", " ")[:200]
#         f1.close()
#         f2 = open(y, 'r', errors="ignore")
#         file_2 = f2.read().replace("\n", " ").replace("\t", " ")[:200]
#         f2.close()

#         result = fuzz.ratio(file_1, file_2)
#         if result > 80:
#             try:
#                 if len(file_2) > len(file_1):
#                     filtered.remove(x)
#                 else:
#                     filtered.remove(y)
#             except:
#                 pass

# print(sorted([x.split(sep)[-1] for x in filtered]))
# print(len(filtered))

# if not exists(DIR_FINAL):
#     makedirs(DIR_FINAL)


# print("Write cleaned files to new dir")
# for source in tqdm(filtered):
#     f = open(source, 'r', errors="ignore")
#     data = f.read().strip()
#     f.close()

#     with open(join(DIR_FINAL, source.split(sep)[-1]), 'w', errors="ignore") as out:
#         out.write(data)

