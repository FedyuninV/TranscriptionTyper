from aqt.editor import Editor
from anki.hooks import wrap, addHook
from aqt.utils import showInfo
from aqt.qt import QMenu, QCursor

class _TextMime:
    def __init__(self, text):
        self._text = text

    def hasText(self):
        return True

    def text(self):
        return self._text

def _onTranscriptionButton(self):
    m = QMenu(self.mw)
    symbols = 'abcde'
    for symbol in symbols:
        a = m.addAction(_(symbol))
        a.triggered.connect(lambda x=symbol: self.doPaste(x, True))
    m.popup(QCursor.pos())

def _addTranscriptionButton(righttopbtns, self):
    self._links['onTranscriptionButton'] = _onTranscriptionButton
    righttopbtns.append(self._addButton(icon='/home/fedyuninv/Documents/MyOwn/Coding/anki/TranscriptionTyping/transcription.png', cmd='onTranscriptionButton', tip="Transcription symbols"))
    return righttopbtns

addHook("setupEditorButtons", _addTranscriptionButton)

