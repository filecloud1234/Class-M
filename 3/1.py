fields = ["math","geography","geometry"]
final_score = []
for i in fields:
    score = int(input(f"Enter Your {i} Score: "))
    if score < 10:
        print(f"you missed the {i}")
        break
    final_score.append(score)

if len(final_score)>1:
    print(sum(final_score)/len(final_score))

# dars=["math","geography","geometry"]
# a=int(input("math score :"))
# b=int(input("geography score :"))
# c=int(input("geometry score :"))
# moadel=m
# m=


# if a<10:
#     print("math:tajdid")
#     if b<10:
#         print("geography:tajdid")
#         if c<10:
#             print("geometry tajdid")
#             if m<15:
#                 print("tajdid")