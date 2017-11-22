from anki.hooks import addHook
from aqt.qt import QMenu, QCursor
from os.path import join


def _on_transcription_button(self):
    """
    Executed when the button on the right top of the editor is pressed.
    Creates popup menu with different phonetics symbols to print.
    """
    m = QMenu(self.mw)
    symbols = "æɑɒɔəɜɪʊʌθðŋɹɫʃʒʍʔ"
    for s in symbols:
        a = m.addAction(_(s))
        a.triggered.connect(lambda ign, _s=s: self.doPaste(_s, True))
    m.popup(QCursor.pos())


def _add_transcription_button(righttopbtns, self):
    """
    Executed when editor base is built.
    Adds button for transcription symbols.
    """
    self._links['onTranscriptionButton'] = _on_transcription_button
    icon_path = join(join(self.mw.pm.addonFolder(), 'TranscriptionTyping'), 'transcription.png')
    transcription_button = self._addButton(icon=icon_path,
                                           cmd='onTranscriptionButton',
                                           tip="Transcription symbols")
    righttopbtns.insert(-1, transcription_button)
    return righttopbtns


# This filter is executed when Anki finished building its editor.
# (since Anki ver. 2.1.*)
addHook("setupEditorButtons", _add_transcription_button)
