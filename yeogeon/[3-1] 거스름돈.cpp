#include <iostream>
#include <array>

using namespace std;

int MySolution( int money );
int BookSolution( int money );

int main()
{
	/*
	예제 3-1 거스름돈
	당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원,
	50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때,
	거슬러 줘야 할 동전의 최소 개수를 구하여라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
	*/

	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;

	cout << "Book's Solution ===========\n";
	cout << BookSolution( p ) << endl << endl;
}

int MySolution( int money )
{
	const array<int, 4> coins{ 500, 100, 50, 10 };
	int coin_cnt{};

	for ( int i{}; i < coins.size(); ++i ) {
		for ( int j{}; ; ++j ) {
			money -= coins[i];
		
			if ( money < 0 ) {
				money += coins[i];
				break;
			}

			++coin_cnt;
		}
	}

	return coin_cnt;
}

int BookSolution( int money )
{
	const array<int, 4> coins{ 500, 100, 50, 10 };
	int coin_cnt{};

	for ( auto coin : coins ) {
		coin_cnt += money / coin;
		money %= coin;
	}

	return coin_cnt;
}