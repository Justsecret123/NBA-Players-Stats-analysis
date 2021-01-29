#ifndef PLAYER_H
#define PLAYER_H

#include <string>

#include <QtCharts/QBarSeries>
#include<QtCharts/QBarSet>
#include <QtCharts/QChart>
#include <QtCharts/QLegend>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
#include <QtCharts/QChartView>

#include <QString>
#include <QStringList>
#include <QFont>
#include <QColor>

class Player
{
public:
    std::string name;
    int points;
    int assists;
    int rebounds;
    int steals;
    int blocks;
    int primary_position;

    Player();

    Player(std::string name, int points, int assists, int rebounds, int steals, int blocks, int primary_position){
        this->name = name;
        this->points = points;
        this->assists = assists;
        this->rebounds = rebounds;
        this->steals = steals;
        this->blocks = blocks;
        this->primary_position = primary_position;
    }

    static QStringList create_list_from_players(Player players[]){

        QStringList list_of_players;

        for(int i=0; i < 3 ; i++){
            list_of_players.append(players[i].name.c_str());
        }

        return list_of_players;
    }

    static int max_element(Player player0, Player player1){

        int max = player0.points;

        //Iteration1: first player
        max = (max>player0.assists)?max:player0.assists;
        max = (max>player0.rebounds)?max:player0.rebounds;
        max = (max>player0.steals)?max:player0.steals;
        max = (max>player0.blocks)?max:player0.blocks;

        //Iteration2: second player
        max = (max>player1.points)?max:player1.points;
        max = (max>player1.assists)?max:player1.assists;
        max = (max>player1.rebounds)?max:player1.rebounds;
        max = (max>player1.steals)?max:player1.steals;
        max = (max>player1.blocks)?max:player1.blocks;

        return max;
    }

    static QtCharts::QChartView *create_comparison_chart (Player player0, Player player1){

        //Players names
        const char* name0 = player0.name.c_str();
        const char* name1 = player1.name.c_str();

        //Max value. Usefulness: range
        int max = max_element(player0, player1);

        //The chart view's font
        QFont *chart_font = new QFont();
        chart_font->setFamily("Segoe UI");
        chart_font->setWeight(300);
        chart_font->setPixelSize(16);

        //Chart view's title
        std::string title;
        title.append(name0);
        title.append(" vs ");

        title.append(name1);
        //First player set
        QtCharts::QBarSet *set0 = new QtCharts::QBarSet(name0);
        *set0 << player0.points << player0.assists << player0.rebounds << player0.steals << player0.blocks;
        set0->setColor(QColor(62, 193, 255));

        //Second player set
        QtCharts::QBarSet *set1 = new QtCharts::QBarSet(name1);
        *set1 << player1.points << player1.assists << player1.rebounds << player1.steals << player1.blocks;
        set1->setColor(QColor(24, 73, 93));

        //Series
        QtCharts::QBarSeries *series = new QtCharts::QBarSeries();
        series->append(set0);
        series->append(set1);

        //Chart
        QtCharts::QChart *chart = new QtCharts::QChart();
        chart->addSeries(series);
        chart->setTitle(title.c_str());

        chart->setAnimationOptions(QtCharts::QChart::SeriesAnimations);

        //Categories
        QStringList categories;
        categories << "Points" << "Assists" << "Rebounds" << "Steals" << "Blocks";

        //Axis X
        QtCharts::QBarCategoryAxis *axisX = new QtCharts::QBarCategoryAxis();
        axisX->append(categories);
        axisX->setTitleFont(*chart_font);
        axisX->setLabelsFont(*chart_font);
        axisX->setGridLineVisible(false);
        chart->addAxis(axisX,Qt::AlignBottom);
        series->attachAxis(axisX);

        //Axis Y
        QtCharts::QValueAxis *axisY = new QtCharts::QValueAxis();
        chart->addAxis(axisY,Qt::AlignLeft);
        axisY->setTitleFont(*chart_font);
        axisY->setLabelsFont(*chart_font);
        axisY->setLabelFormat("%d");
        //axisY->setGridLineVisible(false);
        axisY->setRange(0,max);
        series->attachAxis(axisY);

        //Legend
        chart->legend()->setVisible(true);
        chart->legend()->setAlignment(Qt::AlignBottom);



        chart->legend()->setFont(*chart_font);
        chart->setTitleFont(*chart_font);
        chart->setFont(*chart_font);

        //The chart view itself
        QtCharts::QChartView *chartView = new QtCharts::QChartView(chart);
        chartView->setRenderHint(QPainter::Antialiasing);

        chartView->setFont(*chart_font);



        return chartView;
    }



};


#endif // PLAYER_H
