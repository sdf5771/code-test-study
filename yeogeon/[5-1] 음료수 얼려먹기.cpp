#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <ranges>

using namespace std;

struct Param {
	int n{}, k{};
	vector<vector<int>> v{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n >> p.k;

		char elm{};
		for ( int i{}; i < p.n; ++i ) {
			p.v.push_back( {} );
			for ( int j{}; j < p.k; ++j ) {
				is >> elm;
				p.v[i].push_back( atoi( &elm ));
			}
		}

		return is;
	}
};

using Result = int;

Result MySolution( Param param );
Result BookSolution( Param param );

int main()
{
	int p{};
	cin >> p;

	cout << "My Solution ===========\n";
	cout << MySolution( p ) << endl << endl;

	cout << "Book's Solution ===========\n";
	cout << BookSolution( p ) << endl << endl;
}

Result MySolution( Param param )
{
	Result cnt{};

	constexpr int HOLE{ 0 }, BLOCK{ 1 };

	vector<vector<uint8_t>> frozen(param.n, vector<uint8_t>(param.k, false));

	// dfs 함수
	function<void(int y, int x)> dfs = [&]( int y, int x )
		{
			if ( y < 0 or y >= param.n or x < 0 or x >= param.k ) // y, x 가 범위를 벗어난다면
				return;

			if ( param.v[y][x] == BLOCK )	// 해당 위치가 막혔다면
				return;

			if ( frozen[y][x] == true )
				return;
			
			// 이 위치는 얼은 부분 -> frozen 벡터에 추가
			frozen[y][x] = true;

			// 탐색 시작
			dfs( y, x + 1 );
			dfs( y, x - 1 );
			dfs( y + 1, x );
			dfs( y - 1, x );
		};

	for ( int y : views::iota( 0, param.n ) ) 
		for ( int x : views::iota(0, param.k) )
			if ( frozen[y][x] == false and param.v[y][x] == HOLE ) {
				dfs( y, x );
				++cnt;
			}

	return cnt;
}

Result BookSolution( Param param )
{
	Result cnt{};

	constexpr int HOLE{ 0 }, BLOCK{ 1 };

	// dfs 함수
	function<bool( int y, int x )> dfs = [&]( int y, int x ) -> bool
		{
			if ( y < 0 or y >= param.n or x < 0 or x >= param.k ) // y, x 가 범위를 벗어난다면
				return false;

			if ( param.v[y][x] == HOLE ) {	// 해당 위치가 막혔다면
				param.v[y][x] = BLOCK;

				// 탐색 시작
				dfs( y, x + 1 );
				dfs( y, x - 1 );
				dfs( y + 1, x );
				dfs( y - 1, x );

				return true;
			}

			return false;
		};

	for ( int y : views::iota( 0, param.n ) )
		for ( int x : views::iota( 0, param.k ) )
			if ( dfs( y, x ) )
				++cnt;

	return cnt;
}
