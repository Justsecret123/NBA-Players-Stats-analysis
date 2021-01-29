#include "mainwindow.h"

#include "player.h"

#include <iostream>
#include<QDebug>

#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QLegend>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
#include <QtWidgets/QLabel>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>



QT_CHARTS_USE_NAMESPACE




int main(int argc, char *argv[])
{

    QApplication a(argc, argv);

    Player player1, player2, player3;
    Player list_players[100];

    //                Name     P   A   R    S  B   P
    player1 = Player("LeBron", 10, 10, 10, 10, 10, 10);
    player2 = Player("Kawhi",  10,  5, 24, 45, 130,10);
    player3 = Player("Steph",10,10,10,10,10,10);


   list_players[0] = player1;
   list_players[1] = player2;
   list_players[2] = player3;

   //Players
    QStringList list = Player::create_list_from_players(list_players);

    for (int i=0; i< 3; i++){
        qInfo() << QString(list[i]);
    }




    MainWindow w;

    w.show();

    QTextEdit *text = w.findChild<QTextEdit*>("textEdit_new_player_name");

    text->setText(list[1]);

    QChartView *chart_comparisons = Player::create_comparison_chart(player1, player2);
    QVBoxLayout *layout_comparisons = w.findChild<QVBoxLayout*>("vLayout_comparisons_chart");

    layout_comparisons->addWidget(chart_comparisons);





    return a.exec();



    return 0;



}
