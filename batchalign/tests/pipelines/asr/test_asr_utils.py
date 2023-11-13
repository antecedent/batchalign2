from batchalign.pipelines.asr.utils import *
from batchalign.document import *

RAW_OUTPUT = {'monologues': [{'elements': [{'type': 'text', 'ts': 0.42, 'end_ts': 1.12, 'value': 'uh'}, {'type': 'text', 'ts': 1.12, 'end_ts': 1.56, 'value': 'Py'}, {'type': 'text', 'ts': 1.56, 'end_ts': 2.06, 'value': 'audio'}, {'type': 'text', 'ts': 2.06, 'end_ts': 2.46, 'value': 'uh'}, {'type': 'text', 'ts': 2.46, 'end_ts': 2.9, 'value': 'analysis'}, {'type': 'text', 'ts': 2.9, 'end_ts': 3.3, 'value': 'uh'}, {'type': 'text', 'ts': 3.3, 'end_ts': 3.54, 'value': 'Python'}, {'type': 'text', 'ts': 3.54, 'end_ts': 3.92, 'value': 'library'}, {'type': 'text', 'ts': 3.92, 'end_ts': 4.38, 'value': 'covering'}, {'type': 'text', 'ts': 4.38, 'end_ts': 4.88, 'value': 'uh'}, {'type': 'text', 'ts': 4.88, 'end_ts': 5.18, 'value': 'right'}, {'type': 'text', 'ts': 5.18, 'end_ts': 5.5, 'value': 'range'}, {'type': 'text', 'ts': 5.5, 'end_ts': 5.7, 'value': 'of'}, {'type': 'text', 'ts': 5.7, 'end_ts': 6.08, 'value': 'audio'}, {'type': 'text', 'ts': 6.08, 'end_ts': 6.46, 'value': 'audio'}, {'type': 'text', 'ts': 6.46, 'end_ts': 7.16, 'value': 'analysis'}, {'type': 'text', 'ts': 7.16, 'end_ts': 7.64, 'value': 'tasks'}, {'type': 'text', 'ts': 7.64, 'end_ts': 8.26, 'value': '.'}], 'speaker': 0}]}
ENCODED_OUTPUT = {'content': [{'tier': {'lang': 'en', 'corpus': 'corpus_name', 'id': 'PAR0', 'name': 'Participant0'}, 'content': [{'text': 'uh', 'time': (420, 1120), 'morphology': None, 'dependency': None}, {'text': 'Py', 'time': (1120, 1560), 'morphology': None, 'dependency': None}, {'text': 'audio', 'time': (1560, 2060), 'morphology': None, 'dependency': None}, {'text': 'uh', 'time': (2060, 2460), 'morphology': None, 'dependency': None}, {'text': 'analysis', 'time': (2460, 2900), 'morphology': None, 'dependency': None}, {'text': 'uh', 'time': (2900, 3300), 'morphology': None, 'dependency': None}, {'text': 'Python', 'time': (3300, 3540), 'morphology': None, 'dependency': None}, {'text': 'library', 'time': (3540, 3920), 'morphology': None, 'dependency': None}, {'text': 'covering', 'time': (3920, 4380), 'morphology': None, 'dependency': None}, {'text': 'uh', 'time': (4380, 4880), 'morphology': None, 'dependency': None}, {'text': 'right', 'time': (4880, 5180), 'morphology': None, 'dependency': None}, {'text': 'range', 'time': (5180, 5500), 'morphology': None, 'dependency': None}, {'text': 'of', 'time': (5500, 5700), 'morphology': None, 'dependency': None}, {'text': 'audio', 'time': (5700, 6080), 'morphology': None, 'dependency': None}, {'text': 'audio', 'time': (6080, 6460), 'morphology': None, 'dependency': None}, {'text': 'analysis', 'time': (6460, 7160), 'morphology': None, 'dependency': None}, {'text': 'tasks', 'time': (7160, 7640), 'morphology': None, 'dependency': None}, {'text': '.', 'time': (7640, 8260), 'morphology': None, 'dependency': None}], 'text': None, 'delim': '.', 'alignment': (420, 8260), 'custom_dependencies': []}], 'media': None, 'langs': ['en']}

def test_process_generation():
    doc = Document.model_validate(ENCODED_OUTPUT, strict=True)

    assert process_generation(RAW_OUTPUT, "en") == doc
    

