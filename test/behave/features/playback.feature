Feature: Interactive Playback
  mycroft will control or play back the niv reading audio files when asked


  Scenario: user asks for a random bible chapter
    Given a recitation may or may not be in progress
    When a user asks for a random bible chapter to be recited
    Then mycroft plays a random bible chapter

  Scenario: user asks mycroft to pause the reading
    Given that the audio is already playing
    When user has asked for the recitation to be paused
    Then recitation should be paused

  Scenario: user asks mycroft to resume playback
    Given that the recitation is already paused
    When user has asked for the recitation to be unpaused
    Then recitation should be unpaused

  Scenario: user asks to start playback of a bible book and chapter
    Given a recitation may or may not be in progress
    When the user asks for a bible book and chapter
    Then playback of a recitation Should begin


  Scenario: user asks to start playback of a bible book without a chapter
    Given a recitation may or may not be in progress
    When the user asks for a bible book without a chapter
    Then mycroft should prompt for a chapter and playback of a recitation Should begin