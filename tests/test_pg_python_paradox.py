import unittest
from homer import analyzer
from homer.tests.python_paradox import text


class TestPythonParadox(unittest.TestCase):
    analyzed_text = analyzer.Article("python_paradox", "pg", text)

    def test_total_words(self):
        self.assertEqual(182, TestPythonParadox.analyzed_text.total_words)

    def test_total_paragraphs(self):
        self.assertEqual(3, TestPythonParadox.analyzed_text.total_paragraphs)

    def test_total_sentences(self):
        self.assertEqual(8, TestPythonParadox.analyzed_text.total_sentences)

    def test_average_sentences_in_paragraph(self):
        self.assertEqual(2.67, TestPythonParadox.analyzed_text.avg_sentences_per_para)

    def test_avergae_words_per_sentnece(self):
        self.assertEqual(22.75, TestPythonParadox.analyzed_text.avg_words_per_sentence)

    def test_total_ands(self):
        self.assertEqual(3, TestPythonParadox.analyzed_text.total_and_words)

    def test_intensifiers(self):
        self.assertEqual(0, len(TestPythonParadox.analyzed_text.get_intensifiers()))

    def test_compsulsive_hedgers(self):
        self.assertEqual(0, len(TestPythonParadox.analyzed_text.get_compulsive_hedgers()))

    def test_abstract_nouns(self):
        self.assertEqual(0, len(TestPythonParadox.analyzed_text.get_vague_words()))


if __name__ == "__main__":
    unittest.main()

