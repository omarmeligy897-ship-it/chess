package tic_tac_toe;


import java.awt.CardLayout;


import java.awt.Font;


import java.awt.Color;


import java.awt.Container;


import java.awt.event.ActionListener;


import java.awt.GridLayout;


import java.awt.event.ActionEvent;


import java.awt.event.MouseEvent;


import java.awt.event.ItemEvent;


import java.awt.event.ItemListener;


import javax.swing.JButton;


import java.awt.event.MouseListener;


import java.util.Random;


import javax.swing.JOptionPane;


import javax.swing.ImageIcon;


import javax.swing.JComboBox;


import javax.swing.JLabel;


import javax.swing.JFrame;

import javax.swing.JPanel;

// و بالتالي أصبح إنشاء كائن منه يمثل إنشاء نافذة JFrame يرث من الكلاس Main هنا جعلنا الكلاس


import javax.swing.JTextField;


import javax.swing.SwingUtilities;






public class Main extends JFrame {


JButton startPage_multiPlayer;


// و الأشياء التي سنضعها فيها startPage هنا قمنا بتعريف الـ


JPanel startPage;


JButton startPage_singlePlayer;


    JLabel singlePlayerPage_label;


JButton startPage_settings;


JButton startPage_about;




JButton startPage_exit;


// و الأشياء التي سنضعها فيها singlePlayerPage هنا قمنا بتعريف الـ


JPanel singlePlayerPage;


// و الأشياء التي سنضعها فيها multiPlayerPage هنا قمنا بتعريف الـ


JTextField singlePlayerPage_playerName;


JButton singlePlayerPage_start;


JPanel multiPlayerPage;


JButton singlePlayerPage_back;


    JButton multiPlayerPage_back;


JLabel multiPlayerPage_firstLabel;


JLabel multiPlayerPage_secondLabel;


JTextField multiPlayerPage_firstPlayerName;


JTextField multiPlayerPage_secondPlayerName;

JButton multiPlayerPage_start;
 

JLabel settingsPage_selectedFontSizeLabel;


// و الأشياء التي سنضعها فيها settingsPage هنا قمنا بتعريف الـ


JPanel settingsPage;


JComboBox settingsPage_selectedBoardValue;


JLabel settingsPage_selectedBoardLabel;


    JLabel gamePage_boardBackground;


JComboBox settingsPage_selectedFontSizeValue;


JButton settingsPage_reset;




JButton settingsPage_back;


JPanel gamePage;


// و الأشياء التي سنضعها فيها gamePage هنا قمنا بتعريف الـ


JLabel gamePage_firstPlayerName;


JPanel gamePage_boardPanel;


JLabel[] gamePage_boardLabels;


// هنا قمنا بتعريف نوع الخط و حجم الخط و الألوان التي سنستخدمها في اللعبة


JLabel gamePage_secondPlayerName;


JLabel gamePage_firstPlayerScore;


JLabel gamePage_secondPlayerScore;


JLabel gamePage_currentPlayerIcon;

JButton gamePage_back;

Font defaultFont = new Font("Arial", Font.BOLD, 16);


JButton gamePage_restart;


// سنستخدم هذا المتغير لتحديد ما إذا كان شخص واحد سيلعب اللعبة أو إثنين


Color defaultButtonBackgroundColor = Color.lightGray;


Color defaultButtonTextColor = Color.black;


Color oForeground = Color.red;


Color xForeground = Color.blue;


boolean challengeComputer = false;


Color winnerSquaresBackground = Color.yellow;


    // randomNumber لتوليد أرقام عشوائية عند اللعب ضد الكمبيوتر. و سنخزن الرقم في المتغير random سنستخدم الكائن


// سنستخدم هذا المتغير لتحديد دور من في اللعب


boolean isFirstPlayerTurn = true;


// سنستخدم هذا المتغير لحساب عدد النقرات و بالتالي لتحديد ما إذا كان سيتم إيقاف اللعبة أم لا




int XOCounter = 0;


// سنستخدم هذا المتغير أيضاً لتحديد ما إذا كان سيتم إيقاف اللعبة بسبب فوز أحد اللاعبين


boolean isGameEnds = false;


Random random = new Random();

int randomNumber;
 
 

singlePlayerPage_label.setFont(font);


// سنستخدم هذه الدالة كلما أردنا تغيير حجم خط جميع الأزرار و النصوص الموجودة في اللعبة دفعة واحدة


private void setNewFont(Font font) {


startPage_singlePlayer.setFont(font);


startPage_about.setFont(font);


startPage_multiPlayer.setFont(font);

startPage_settings.setFont(font);

        settingsPage_selectedBoardValue.setFont(font);

startPage_exit.setFont(font);
        singlePlayerPage_playerName.setFont(font);

singlePlayerPage_start.setFont(font);


multiPlayerPage_firstLabel.setFont(font);


singlePlayerPage_back.setFont(font);


multiPlayerPage_firstPlayerName.setFont(font);


multiPlayerPage_secondLabel.setFont(font);


multiPlayerPage_start.setFont(font);


multiPlayerPage_secondPlayerName.setFont(font);

multiPlayerPage_back.setFont(font);

        gamePage_back.setFont(font);


settingsPage_selectedBoardLabel.setFont(font);


settingsPage_selectedFontSizeLabel.setFont(font);


settingsPage_reset.setFont(font);


settingsPage_selectedFontSizeValue.setFont(font);

settingsPage_back.setFont(font);

gamePage_secondPlayerName.setFont(font);


gamePage_boardPanel.setFont(font);


gamePage_firstPlayerName.setFont(font);


gamePage_firstPlayerScore.setFont(font);


        startPage_multiPlayer.setBackground(backgroundColor);


gamePage_secondPlayerScore.setFont(font);

gamePage_restart.setFont(font);
 
    }
 

    // سنستخدم هذه الدالة كلما أردنا تغيير ألوان أزرار التطبيق


private void setThemeColors(Color textColor, Color backgroundColor) {




startPage_singlePlayer.setForeground(textColor);


startPage_settings.setForeground(textColor);


startPage_multiPlayer.setForeground(textColor);

startPage_about.setForeground(textColor);

startPage_settings.setBackground(backgroundColor);


startPage_exit.setForeground(textColor);


startPage_singlePlayer.setBackground(backgroundColor);


multiPlayerPage_firstPlayerName.setForeground(textColor);


startPage_about.setBackground(backgroundColor);


startPage_exit.setBackground(backgroundColor);


singlePlayerPage_label.setForeground(textColor);




singlePlayerPage_playerName.setForeground(textColor);


singlePlayerPage_start.setForeground(textColor);


singlePlayerPage_start.setBackground(backgroundColor);


singlePlayerPage_back.setForeground(textColor);


multiPlayerPage_firstLabel.setForeground(textColor);


singlePlayerPage_back.setBackground(backgroundColor);


gamePage_secondPlayerScore.setForeground(textColor);


multiPlayerPage_secondLabel.setForeground(textColor);


multiPlayerPage_secondPlayerName.setForeground(textColor);


multiPlayerPage_start.setForeground(textColor);


multiPlayerPage_start.setBackground(backgroundColor);


multiPlayerPage_back.setForeground(textColor);


gamePage_firstPlayerName.setForeground(textColor);


multiPlayerPage_back.setBackground(backgroundColor);


gamePage_firstPlayerScore.setForeground(textColor);


gamePage_secondPlayerName.setForeground(textColor);

gamePage_back.setForeground(textColor);

settingsPage_reset.setBackground(backgroundColor);


gamePage_restart.setForeground(textColor);


gamePage_restart.setBackground(backgroundColor);


gamePage_back.setBackground(backgroundColor);


settingsPage_selectedBoardLabel.setForeground(textColor);


settingsPage_selectedBoardValue.setForeground(textColor);


settingsPage_selectedFontSizeValue.setForeground(textColor);


settingsPage_selectedFontSizeLabel.setForeground(textColor);

settingsPage_reset.setForeground(textColor);

        startPage.add(startPage_settings);


settingsPage_back.setForeground(textColor);


settingsPage_back.setBackground(backgroundColor);

}
 
 

// startPage سنستخدم هذه الدالة لخلق محتوى الصفحة


private void createStartPage() {


// هنا أنشأنا الحاوية الأساسية و الأشياء التي سنضعها فيها


startPage = new JPanel(null);


startPage_singlePlayer = new JButton("Single Player");


startPage_settings = new JButton("Settings");


startPage_multiPlayer = new JButton("Multi Player");

startPage_about = new JButton("About");

        startPage.add(startPage_about);

startPage_exit = new JButton("Exit");
 

// هنا وضعنا كل شيء بداخل الحاوية


startPage.add(startPage_singlePlayer);

startPage.add(startPage_multiPlayer);

singlePlayerPage_label = new JLabel("Player Name");


startPage.add(startPage_exit);




// هنا قمنا بتحديد حجم و موقع كل شيء أضفناه في الحاوية


startPage_singlePlayer.setBounds(80, 110, 240, 40);


startPage_settings.setBounds(80, 230, 240, 40);


startPage_multiPlayer.setBounds(80, 170, 240, 40);

startPage_about.setBounds(80, 290, 240, 40);

// singlePlayerPage سنستخدم هذه الدالة لخلق محتوى الصفحة


startPage_exit.setBounds(80, 350, 240, 40);

}
 
 

        singlePlayerPage_playerName = new JTextField("player");

private void createSinglePlayerPage() {
 

// هنا أنشأنا الحاوية الأساسية و الأشياء التي سنضعها فيها

singlePlayerPage = new JPanel(null);

}


singlePlayerPage_start = new JButton("Start");


singlePlayerPage_back = new JButton("Back");


singlePlayerPage.add(singlePlayerPage_label);


// هنا وضعنا كل شيء بداخل الحاوية


singlePlayerPage.add(singlePlayerPage_start);


singlePlayerPage.add(singlePlayerPage_playerName);


// هنا قمنا بتحديد حجم و موقع كل شيء أضفناه في الحاوية


singlePlayerPage.add(singlePlayerPage_back);


singlePlayerPage_playerName.setBounds(190, 170, 130, 30);


singlePlayerPage_label.setBounds(80, 170, 100, 30);


singlePlayerPage_back.setBounds(80, 280, 240, 40);


singlePlayerPage_start.setBounds(80, 220, 240, 40);


multiPlayerPage.add(multiPlayerPage_secondLabel);


// multiPlayerPage سنستخدم هذه الدالة لخلق محتوى الصفحة


private void createMultiPlayerPage() {


// هنا أنشأنا الحاوية الأساسية و الأشياء التي سنضعها فيها


multiPlayerPage = new JPanel(null);


multiPlayerPage_firstLabel = new JLabel("Player X");


multiPlayerPage_firstPlayerName = new JTextField("player 1", 8);


multiPlayerPage_secondLabel = new JLabel("Player O");


multiPlayerPage_secondPlayerName = new JTextField("player 2", 8);


multiPlayerPage.add(multiPlayerPage_firstLabel);


multiPlayerPage_start = new JButton("Start");

multiPlayerPage_back = new JButton("Back");
 

    private void createSettingsPage() {

// هنا وضعنا كل شيء بداخل الحاوية

multiPlayerPage.add(multiPlayerPage_firstPlayerName);


multiPlayerPage.add(multiPlayerPage_secondPlayerName);


multiPlayerPage.add(multiPlayerPage_start);


// هنا قمنا بتحديد حجم و موقع كل شيء أضفناه في الحاوية


multiPlayerPage.add(multiPlayerPage_back);


multiPlayerPage_firstPlayerName.setBounds(160, 130, 160, 30);


multiPlayerPage_firstLabel.setBounds(80, 130, 70, 30);


multiPlayerPage_secondPlayerName.setBounds(160, 190, 160, 30);


multiPlayerPage_secondLabel.setBounds(80, 190, 70, 30);

multiPlayerPage_start.setBounds(80, 250, 240, 40);



multiPlayerPage_back.setBounds(80, 310, 240, 40);

}
 
 

        settingsPage.add(settingsPage_selectedBoardValue);

// settingsPage سنستخدم هذه الدالة لخلق محتوى الصفحة

// هنا أنشأنا الحاوية الأساسية و الأشياء التي سنضعها فيها


settingsPage = new JPanel(null);


settingsPage_selectedBoardLabel = new JLabel("Game Board");


settingsPage_selectedBoardValue = new JComboBox(new String[]{"Board 1", "Board 2", "Board 3", "Board 4"});


settingsPage_selectedFontSizeLabel = new JLabel("Font Size");


settingsPage_selectedFontSizeValue.setSelectedIndex(1);


settingsPage_selectedFontSizeValue = new JComboBox(new String[]{"Small", "Meduim", "Large"});

settingsPage_reset = new JButton("Reset Default Settings");

settingsPage.add(settingsPage_selectedFontSizeLabel);


settingsPage_back = new JButton("Back");

// هنا وضعنا كل شيء بداخل الحاوية

settingsPage.add(settingsPage_selectedBoardLabel);


gamePage = new JPanel(null);


settingsPage.add(settingsPage_selectedFontSizeValue);


settingsPage.add(settingsPage_reset);


// هنا قمنا بتحديد حجم و موقع كل شيء أضفناه في الحاوية


settingsPage.add(settingsPage_back);


settingsPage_selectedBoardValue.setBounds(200, 130, 120, 30);


settingsPage_selectedBoardLabel.setBounds(80, 130, 100, 30);


settingsPage_selectedFontSizeValue.setBounds(200, 190, 120, 30);


settingsPage_selectedFontSizeLabel.setBounds(80, 190, 100, 30);

settingsPage_reset.setBounds(80, 250, 240, 40);

private void createGamePage() {


settingsPage_back.setBounds(80, 310, 240, 40);

}
 
 

        for (int i = 0; i < gamePage_boardLabels.length; i++) {

// gamePage سنستخدم هذه الدالة لخلق محتوى الصفحة
 

// هنا أنشأنا الحاوية الأساسية و الأشياء التي سنضعها فيها

gamePage_firstPlayerName = new JLabel("", JLabel.CENTER);

gamePage_secondPlayerName = new JLabel("", JLabel.CENTER);


gamePage_firstPlayerScore = new JLabel("0", JLabel.CENTER);


gamePage_secondPlayerScore = new JLabel("0", JLabel.CENTER);


gamePage_currentPlayerIcon = new JLabel("", JLabel.CENTER);


gamePage_boardPanel = new JPanel(new GridLayout(3, 3, 8, 8));


gamePage_boardLabels = new JLabel[9];

gamePage_back = new JButton("Back");

// JLabels التي سنضع فيها 9 gamePage_boardPanel فقط لوضع الصورة خلف الـ Label سنستخدم هذا الـ


gamePage_restart = new JButton("Restart");

gamePage_boardBackground = new JLabel();
 

// مع تحديد بعض خصائصهم gamePage_boardPanel في الحاوية JLabels هنا وضعنا الـ 9


gamePage_boardBackground.setIcon(new ImageIcon(this.getClass().getResource("/images/board_1.png")));

gamePage_boardLabels[i] = new JLabel("", JLabel.CENTER);

// هنا قمنا بتحديد حجم و موقع كل شيء أضفناه في الحاوية


gamePage_boardLabels[i].setFont(new Font("Arial", Font.BOLD, 40));


gamePage_boardLabels[i].setBackground(winnerSquaresBackground);     // Opaque ملحوظة: هذا اللون لن يظهر إلى إذا جعلنا الخلفية صلبة


gamePage_boardPanel.add(gamePage_boardLabels[i]);

}
 

// هنا وضعنا كل شيء بداخل الحاوية


// هنا قمنا بمناداة هذه الدالة لتحديد رمز اللاعب الذي سيلعب الآن على حسب دوره

setCurrentPlayerIcon();
 

gamePage.add(gamePage_secondPlayerScore);


gamePage.add(gamePage_firstPlayerName);


gamePage.add(gamePage_secondPlayerName);

gamePage.add(gamePage_firstPlayerScore);

gamePage.add(gamePage_back);


gamePage.add(gamePage_currentPlayerIcon);

gamePage.add(gamePage_boardBackground);

gamePage.add(gamePage_restart);

gamePage.add(gamePage_boardPanel);
 

    // لجعل لون خلفية المربعات التي كانت سبب فوز الاعب ملونة colorBackgroundWinnerLabels في حال كان يوجد فائز سيتم مناداة الدالة


gamePage_firstPlayerName.setBounds(0, 10, 150, 30);


gamePage_secondPlayerName.setBounds(250, 10, 150, 30);


gamePage_secondPlayerScore.setBounds(250, 40, 150, 30);


gamePage_firstPlayerScore.setBounds(0, 40, 150, 30);


gamePage_boardBackground.setBounds(45, 105, 300, 300);


gamePage_currentPlayerIcon.setBounds(120, 25, 150, 30);

gamePage_boardPanel.setBounds(45, 105, 300, 300);

// سنستخدم هذه الدالة لإظهار لون خلفية المربعات التي بسببها فاز اللاعب و لإيقاف اللعبة


gamePage_back.setBounds(20, 475, 140, 30);


gamePage_restart.setBounds(230, 475, 140, 30);

}
 
 

isGameEnds = true;


private void colorBackgroundWinnerLabels(JLabel l1, JLabel l2, JLabel l3) {

l1.setOpaque(true);
        l2.setOpaque(true);

            colorBackgroundWinnerLabels(gamePage_boardLabels[0], gamePage_boardLabels[1], gamePage_boardLabels[2]);

l3.setOpaque(true);
    }
 
 

// سنستخدم هذه الدالة في كل مرة يلعب فيها اللاعبون للتأكد إذا كان هناك فائز أم لا


// لإيقاف اللعبة. و سيتم إضافة واحد في نتيجة اللاعب الفائز true إلى isGameEnds و لتغيير قيمة المتغير


private void checkIfThereIsAWinner() {




String c0 = gamePage_boardLabels[0].getText();


String c1 = gamePage_boardLabels[1].getText();


String c3 = gamePage_boardLabels[3].getText();


String c2 = gamePage_boardLabels[2].getText();

String c4 = gamePage_boardLabels[4].getText();

String c7 = gamePage_boardLabels[7].getText();


String c5 = gamePage_boardLabels[5].getText();

String c6 = gamePage_boardLabels[6].getText();

        int secondPlayerScore = Integer.valueOf(gamePage_secondPlayerScore.getText());

String c8 = gamePage_boardLabels[8].getText();
 

int firstPlayerScore = Integer.valueOf(gamePage_firstPlayerScore.getText());

if (c0.equals(c1) && c0.equals(c2) && !c0.equals("")) {

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


if (c0.equals("X"))


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else
        }
 

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


if (c3.equals(c4) && c3.equals(c5) && !c3.equals("")) {


if (c3.equals("X"))


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");


else


gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


colorBackgroundWinnerLabels(gamePage_boardLabels[3], gamePage_boardLabels[4], gamePage_boardLabels[5]);


}


if (c6.equals(c7) && c6.equals(c8) && !c6.equals("")) {

if (c6.equals("X"))

gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else

if (c0.equals(c3) && c0.equals(c6) && !c0.equals("")) {


gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


colorBackgroundWinnerLabels(gamePage_boardLabels[6], gamePage_boardLabels[7], gamePage_boardLabels[8]);

}
 
            if (c0.equals("X"))

                gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else

colorBackgroundWinnerLabels(gamePage_boardLabels[0], gamePage_boardLabels[3], gamePage_boardLabels[6]);


}


if (c1.equals(c4) && c1.equals(c7) && !c1.equals("")) {

if (c1.equals("X"))

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else

if (c2.equals(c5) && c2.equals(c8) && !c2.equals("")) {


colorBackgroundWinnerLabels(gamePage_boardLabels[1], gamePage_boardLabels[4], gamePage_boardLabels[7]);

}
 
            if (c2.equals("X"))

colorBackgroundWinnerLabels(gamePage_boardLabels[2], gamePage_boardLabels[5], gamePage_boardLabels[8]);


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");

}
 

                pressedLabel.setForeground(oForeground);


if (c0.equals(c4) && c0.equals(c8) && !c0.equals("")) {

if (c0.equals("X"))
            else

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


colorBackgroundWinnerLabels(gamePage_boardLabels[0], gamePage_boardLabels[4], gamePage_boardLabels[8]);


}


if (c2.equals(c4) && c2.equals(c6) && !c2.equals("")) {

if (c2.equals("X"))

gamePage_secondPlayerScore.setText((secondPlayerScore+1)+"");


gamePage_firstPlayerScore.setText((firstPlayerScore+1)+"");

else

// نستخدم هذه الدالة لتحديد دور اللاعب الحالي في حال كان هناك شخصين يلعبان اللعبة


colorBackgroundWinnerLabels(gamePage_boardLabels[2], gamePage_boardLabels[4], gamePage_boardLabels[6]);

}
 
        gamePage.repaint();
    }
 
 

pressedLabel.setForeground(xForeground);


private boolean isTowPlayerGameEnds(JLabel pressedLabel) {

if (pressedLabel.getText().equals("")) {
 

pressedLabel.setText("X");

if (isFirstPlayerTurn == true) {

                        gamePage_boardLabels[randomNumber].setForeground(oForeground);


isFirstPlayerTurn = false;

} else {

                isFirstPlayerTurn = true;

pressedLabel.setText("O");
            }

            checkIfThereIsAWinner();

gamePage.repaint();

            if (XOCounter == 9 || isGameEnds == true) {

XOCounter++;

                XOCounter = 0;

removeXOListener();

    // نستخدم هذه الدالة لتحديد كيف سيلعب الكمبيوتر في حال كان شخص واحد يلعب اللعبة

}
        }
 

return isGameEnds;

}
 
 

if (XOCounter < 9 && pressedLabel.getText().equals("")) {


private boolean isOnePlayerGameEnds(JLabel pressedLabel) {


XOCounter++;


pressedLabel.setText("X");


pressedLabel.setForeground(xForeground);


if (XOCounter < 9 && isGameEnds == false) {


repaint();


checkIfThereIsAWinner();

for (;;) {

if (gamePage_boardLabels[randomNumber].getText().equals("")) {


randomNumber = random.nextInt(9);


gamePage_boardLabels[randomNumber].setText("O");


    // XOListener هنا قمنا بتحديد ما يحدث عندما يقوم المستخدم بالنقر على أزرار الفأرة في الكائن


gamePage.repaint();

XOCounter++;

checkIfThereIsAWinner();


break;


}


}

}
 

        if (XOCounter >= 9 || isGameEnds == true) {

}
 

removeXOListener();


}


repaint();


return true;


// غير قابلين للنقر عند إيقاف اللعبة Label نستخدم هذه الدالة لجعل الـ


return false;

}
 

private void removeXOListener() {


gamePage_boardLabel.removeMouseListener(XOListener);


for (JLabel gamePage_boardLabel : gamePage_boardLabels) {

}
    }
 

if (isFirstPlayerTurn == true) {


// سنستخدم هذه الدالة لتحديد رمز اللاعب الذي سيلعب الآن على حسب دوره

private void setCurrentPlayerIcon() {

gamePage_currentPlayerIcon.setText("O");


gamePage_currentPlayerIcon.setText("X");


gamePage_currentPlayerIcon.setForeground(xForeground);

}
        else {

@Override


gamePage_currentPlayerIcon.setForeground(oForeground);

}
        repaint();
    }
 
 

public void mousePressed(MouseEvent e) {

MouseListener XOListener = new MouseListener() {

gamePage_boardLabels[6].setOpaque(false);


JLabel pressedLabel = (JLabel) e.getSource();


if (isGameEnds == false) {


isOnePlayerGameEnds(pressedLabel);


if (challengeComputer == true)


isTowPlayerGameEnds(pressedLabel);


else if (challengeComputer == false)

}
        }
 
        @Override

public void mouseReleased(MouseEvent e) { }


public void mouseClicked(MouseEvent e) { }

@Override
 
        @Override


public void mouseEntered(MouseEvent e) { }

// XOListener نستخدم هذه الدالة عند بدء تحديد جديد لتصفير لوح اللعب و ربط الفأرة بالكائن


@Override


public void mouseExited(MouseEvent e) { }

};
 
 
    private void startNewGame() {
 

        gamePage_boardLabels[2].setOpaque(false);

isGameEnds = false;
        XOCounter = 0;

setCurrentPlayerIcon();


gamePage_boardLabels[0].setOpaque(false);

gamePage_boardLabels[1].setOpaque(false);

gamePage_boardLabels[7].setOpaque(false);


gamePage_boardLabels[3].setOpaque(false);

gamePage_boardLabels[4].setOpaque(false);

    // هذه الدالة تقوم ببناء كل شيء في اللعبة و تحدد ماذا سيحدث عندما يتفاعل المستخدم مع محتوى النافذة

gamePage_boardLabels[5].setOpaque(false);

gamePage_boardLabels[8].setOpaque(false);




gamePage_boardLabels[0].setText("");


gamePage_boardLabels[2].setText("");


gamePage_boardLabels[1].setText("");

gamePage_boardLabels[3].setText("");

gamePage_boardLabels[6].setText("");


gamePage_boardLabels[4].setText("");

gamePage_boardLabels[5].setText("");

        gamePage_boardLabels[1].addMouseListener(XOListener);

gamePage_boardLabels[7].setText("");
        gamePage_boardLabels[8].setText("");

gamePage_boardLabels[0].addMouseListener(XOListener);

repaint();
 

gamePage_boardLabels[4].addMouseListener(XOListener);


gamePage_boardLabels[2].addMouseListener(XOListener);

gamePage_boardLabels[3].addMouseListener(XOListener);

    }

gamePage_boardLabels[5].addMouseListener(XOListener);
        gamePage_boardLabels[6].addMouseListener(XOListener);

gamePage_boardLabels[8].addMouseListener(XOListener);

gamePage_boardLabels[7].addMouseListener(XOListener);
 
 
 

        setNewFont(defaultFont);


// فقط createAndShowGUI() سيقوم الكونستركتور بإستدعاء الدالة Main عند إنشاء كائن من الكلاس

public Main() {
        createAndShowGUI();
    }
 
 

 

private void createAndShowGUI() {

// هنا قمن بإستدعاء الدوال التي ستخلق جميع الصفحات في البرنامج


createStartPage();


createSinglePlayerPage();


createGamePage();


createMultiPlayerPage();

createSettingsPage();
 

CardLayout card = new CardLayout();


// لجعل الصفحات موضوعة وراء بعضها البعض CardLayout هنا جعلنا النافذة تستخدم الـ

Container container = getContentPane();

add(multiPlayerPage);


container.setLayout(card);


// هنا أضفنا جميع الصفحات (الحاويات) في النافذة

add(startPage);
        add(singlePlayerPage);

container.getLayout().addLayoutComponent("startPage", startPage);


add(settingsPage);

add(gamePage);
 

// هنا وضعنا إسم لكل صفحة (حاوية) لنصبح قادرين على تحديد الصفحة التي سيتم عرضها من خلال إسمها


container.getLayout().addLayoutComponent("settingsPage", settingsPage);


container.getLayout().addLayoutComponent("singlePlayerPage", singlePlayerPage);

container.getLayout().addLayoutComponent("multiPlayerPage", multiPlayerPage);

        startPage_about.addActionListener(new ActionListener() {


container.getLayout().addLayoutComponent("gamePage", gamePage);


setThemeColors(defaultButtonTextColor, defaultButtonBackgroundColor);


// لجعلهم قابلين للنقر XOListener بالكائن Labels هنا ربطنا الـ 9


for (JLabel gamePage_boardLabel : gamePage_boardLabels) {




gamePage_boardLabel.addMouseListener(XOListener);

}
 

startPage_singlePlayer.addActionListener(new ActionListener() {


// تظهر كأول صفحة في النافذة startPage هنا جعلنا الحاوية

@Override

});


public void actionPerformed(ActionEvent e) {


card.show(container, "singlePlayerPage");

}
 
 

startPage_multiPlayer.addActionListener(new ActionListener() {


// ظاهرة multiPlayerPage يجعل الحاوية startPage_multiPlayer هنا جعلنا الزر

@Override
            public void actionPerformed(ActionEvent e) {

            public void actionPerformed(ActionEvent e) {

card.show(container, "multiPlayerPage");
            }


});
 
// ظاهرة settingsPage يجعل الحاوية startPage_settings هنا جعلنا الزر

startPage_settings.addActionListener(new ActionListener() {
            @Override

                        = "


card.show(container, "settingsPage");

}
        });

// يعرض نافذة منبثقة فيها بعض المعلومات حول اللعبة startPage_about هنا جعلنا الزر

@Override

public void actionPerformed(ActionEvent e) {
String aboutGame
