from anki.hooks import addHook
from aqt.qt import QMenu, QCursor
from os.path import join


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
    transcription_button = self._addButton(icon=icon_path,
                                           cmd='onTranscriptionButton',
                                           tip="Transcription symbols")
    righttopbtns.insert(-1, transcription_button)
    return righttopbtns


addHook("setupEditorButtons", _addTranscriptionButton)
