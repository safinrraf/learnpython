from unittest import TestCase

from start.leetcode.daily.u202411.easy.delete_characters_to_make_fancy_string import DeleteCharactersToMakeFancyString


class TestSolution(TestCase):
    def test_make_fancy_string1(self):
        input1 = "leeetcodeeeeeeeeeeeeeeeeeeeeeedddddddddddddddddddddd"
        expected = "leetcodeedd"
        result = DeleteCharactersToMakeFancyString.makeFancyString(input1)
        self.assertEqual(expected, result)

    def test_make_fancy_string2(self):
        input2 = "aaabaaaa"
        expected = "aabaa"
        result = DeleteCharactersToMakeFancyString.makeFancyString(input2)
        self.assertEqual(expected, result)

    def test_make_fancy_string3(self):
        input3 = ("aaabaaaahgdkjzgfbdsjlhzvbldjfvhjjjjjjjjjjjjjjjjjjjjjjjjjgzzzzzzzzzzzzzzzzzzzzzzcbvhgvhgvkhgkvhgv"
                  "khgvhgkvkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkvvvvvvvvvvvvvvvvvvvvvvvvvvvvgggggggggggggggggg"
                  "ffffffffffffffffffffffdddddddddddddddddddddddddddffffffffffffffffffffffffffffffffgggggggggggggg"
                  "gggggggggggggccccccccccccccccccccccccfffffffffffffffffffffdddddddddddddddfgjdhdhgfghfhjgfjhgfhgf"
                  "hgggggggggggggggggggggggggggggggggggffdddddddddddddxcccccccccccccccccccccxxxxxxxxxxxxxxxxxxxxxxxx"
                  "xxxxxzzzzzzzzzzzzzzzzzzzzzzzzsssssssssssssssssssssssssswwwwwwwwwwwwwwwwwdfffdfdgfdgfdgfghfhgfhgfh"
                  "ghgfhgfhghgfhghfhgfhgfhgfgfhgfhgfhgfhghfhgfhgfhghfhgfjhjfhjgfjhgfjhgjfcjgfcjgfxjgxdfdfxgcvvcxvcxv"
                  "cxdxfdxfgdgfdcgfhgfhgvhg")
        expected = ("aabaahgdkjzgfbdsjlhzvbldjfvhjjgzzcbvhgvhgvkhgkvhgvkhgvhgkvkkvvggffddffggccffddfgjdhdhgfghfhjgfj"
                    "hgfhgfhggffddxccxxzzsswwdffdfdgfdgfdgfghfhgfhgfhghgfhgfhghgfhghfhgfhgfhgfgfhgfhgfhgfhghfhgfhgfh"
                    "ghfhgfjhjfhjgfjhgfjhgjfcjgfcjgfxjgxdfdfxgcvvcxvcxvcxdxfdxfgdgfdcgfhgfhgvhg")
        result = DeleteCharactersToMakeFancyString.makeFancyString(input3)
        self.assertEqual(expected, result)

    def test_make_fancy_string4(self):
        input4 = "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
        expected = "uu"
        result = DeleteCharactersToMakeFancyString.makeFancyString(input4)
        self.assertEqual(expected, result)