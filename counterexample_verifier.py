'''
This is the smallest counterexample - this isn't the code that generated it, this
file is just to explain and verify it.

To run this program, use command:
$ python counterexample_verifier.py


The counterexample is:
'''
k=163

'''
sqrt(2*163) = 18.05, therefore:
'''
P   = 17
P_1 = 13
P_2 = 11
P_3 = 7
P_4 = 5
P_5 = 3

'''
(we won't need P_6)

The list P_5_pairs contains the pairs containing multiples of P,...,P_5 that are
not prime (i.e not 1*P_i).
'''
P_5_pairs = [(1, 325), (2, 324), (3, 323), (4, 322), (5, 321), (6, 320), (7, 319), (8, 318), (9, 317), (10, 316), (11, 315), (12, 314), (14, 312), (15, 311), (16, 310), (17, 309), (18, 308), (20, 306), (21, 305), (22, 304), (23, 303), (24, 302), (25, 301), (26, 300), (27, 299), (28, 298), (29, 297), (30, 296), (31, 295), (32, 294), (33, 293), (34, 292), (35, 291), (36, 290), (37, 289), (38, 288), (39, 287), (40, 286), (41, 285), (42, 284), (44, 282), (45, 281), (46, 280), (47, 279), (48, 278), (49, 277), (50, 276), (51, 275), (52, 274), (53, 273), (54, 272), (55, 271), (56, 270), (57, 269), (59, 267), (60, 266), (61, 265), (62, 264), (63, 263), (65, 261), (66, 260), (67, 259), (68, 258), (69, 257), (70, 256), (71, 255), (72, 254), (73, 253), (74, 252), (75, 251), (76, 250), (77, 249), (78, 248), (79, 247), (80, 246), (81, 245), (83, 243), (84, 242), (85, 241), (86, 240), (87, 239), (88, 238), (89, 237), (90, 236), (91, 235), (92, 234), (93, 233), (95, 231), (96, 230), (98, 228), (99, 227), (100, 226), (101, 225), (102, 224), (104, 222), (105, 221), (106, 220), (107, 219), (108, 218), (109, 217), (110, 216), (111, 215), (112, 214), (113, 213), (114, 212), (115, 211), (116, 210), (117, 209), (118, 208), (119, 207), (120, 206), (121, 205), (122, 204), (123, 203), (125, 201), (126, 200), (128, 198), (129, 197), (130, 196), (131, 195), (132, 194), (133, 193), (134, 192), (135, 191), (136, 190), (137, 189), (138, 188), (139, 187), (140, 186), (141, 185), (143, 183), (144, 182), (145, 181), (146, 180), (147, 179), (149, 177), (150, 176), (151, 175), (152, 174), (153, 173), (154, 172), (155, 171), (156, 170), (157, 169), (158, 168), (159, 167), (160, 166), (161, 165), (162, 164)]

'''
The following code verifies that:
- Every element of P_5_pairs is distinct
- Every pair (a,b) in P_5_pairs is ordered such that a<b
- Every element of P_5_pairs sums to 2*k
- Every element of P_5_pairs contains a number that is equal to p*n, where:
    - p is equal to P, P_1, ..., or P_5
    - n is an integer and n >= 2
'''
for i in range(len(P_5_pairs)):
    for j in range(len(P_5_pairs)):
        if i != j  and  P_5_pairs[i] == P_5_pairs[j]:
            print("VERIFICATION FAILED:")
            print(f"P_5_pairs contains a duplicate: elements {i} and {j} are both {P_5_pairs[i]}")
            exit(1)
print("Verified everything in P_5_pairs is distinct")

for pair in P_5_pairs:
    if pair[0] >= pair[1]:
        print("VERIFICATION FAILED:")
        print(f"P_5_pairs contains pair {pair} which is not ascending.")
        exit(1)
print(f"Verified each pair (a,b) in P_5_pairs is ordered such that a<b")

for pair in P_5_pairs:
    if pair[0] + pair[1] != 2*k:
        print("VERIFICATION FAILED:")
        print(f"P_5_pairs contains pair {pair} which does not sum to 2*{k}")
        exit(1)
print(f"Verified each pair in P_5_pairs sums to 2*{k}")

for pair in P_5_pairs:
    is_multiple = False
    for P_i in [P, P_1, P_2, P_3, P_4, P_5]:
        if  ((
                pair[0]%P_i == 0        # Checking divisibility by P_i
                and not pair[0] == P_i  # Checking not equal to P_i, which would make it prime
            ) or (
                pair[1]%P_i == 0        # Making the same checks for the other number in the pair
                and not pair[1] == P_i
            )):
            # If this line is reached, then this pair contains a non-prime multiple of P_i.
            is_multiple = True
            break
    if not is_multiple:
        print("VERIFICATION FAILED:")
        print(f"P_5_pairs contains pair {pair} which does not contain a non-prime multiple of any P,...,P_5")
        exit(1)
print(f"Verified all pairs in P_5_pairs contain a non-prime multiple of P, ... or, P_5")


'''
According to Proposition C:
    k - len(P_5_pairs)  >=  k * (1-2/P) * (1-2/P_1) * ... * (1-2/P_5)

This is false, as verified by the following code:
'''
lhs  =  k - len(P_5_pairs)
rhs  =  k * (1-2/P) * (1-2/P_1) * (1-2/P_2) * (1-2/P_3) * (1-2/P_4) * (1-2/P_5)
print(f"Proposition C implies that:  {lhs} >= {rhs}")
