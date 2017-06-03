from anki.hooks import wrap, addHook
from aqt.qt import QMenu, QCursor
from os.path import join

class _TextMime:
    def __init__(self, text):
        self._text = text

    def hasText(self):
        return True

    def text(self):
        return self._text

def _onTranscriptionButton(self):
    m = QMenu(self.mw)
    symbols = "æɑɒɔəɜɪʊʌθðŋɹɫʃʒʍʔ"
    for s in symbols:
        a = m.addAction(_(s))
        a.triggered.connect(lambda ign, _s=s: self.doPaste(_s, True))
    m.popup(QCursor.pos())

def _addTranscriptionButton(righttopbtns, self):
    self._links['onTranscriptionButton'] = _onTranscriptionButton
    icon_path = join(self.mw.pm.addonFolder(), 'transcription.png')
    righttopbtns.append(self._addButton(icon=icon_path,
                                        cmd='onTranscriptionButton',
                                        tip="Transcription symbols"))
    return righttopbtns

addHook("setupEditorButtons", _addTranscriptionButton)

