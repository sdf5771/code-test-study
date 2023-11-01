#include <iostream>
#include <queue>
#include <vector>
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
				p.v[i].push_back( atoi( &elm ) );
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
	constexpr int MONSTER{ 0 }, ROAD{ 1 };

	enum DIR { N, E, S, W, DIR_CNT };
	struct POS { int y{}, x{}; };
	const POS dirs[]{ { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	vector<vector<int>> min_dist( param.n, vector<int>( param.k, 0 ) );

	function<void( int, int, int, DIR )> dfs = [&]( int y, int x, int prev_dist, DIR from_dir ) {
		if ( y < 0 or x < 0 or y >= param.n or x >= param.k )
			return;

		if ( param.v[y][x] == MONSTER )
			return;

		int& cur_dist = min_dist[y][x];
		if ( cur_dist == 0 or cur_dist >= prev_dist )
			cur_dist = prev_dist + 1;
		else
			return;
		
		// debug
		//system( "pause>null" );
		//cout << endl;
		//for ( int i{}; i < param.n; ++i ) {
		//	for ( int j{}; j < param.m; ++j )
		//		cout << format( "{:2}", min_dist[i][j] );
		//	cout << endl;
		//}

		for ( int i{}; i < DIR_CNT; ++i ) {
			int new_y{ y + dirs[i].y };
			int new_x{ x + dirs[i].x };

			if ( from_dir != DIR(i) )
				dfs( new_y, new_x, cur_dist, DIR( ( i + 2 ) % DIR_CNT ) );
		}
	};

	dfs( 0, 0, 0, DIR_CNT );

	return min_dist.back().back();
}

Result BookSolution( Param param )
{
	constexpr int MONSTER{ 0 }, ROAD{ 1 };

	struct POS { int y{}, x{}; };
	const POS dirs[]{ { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	vector<vector<int>> min_dist{ param.v };

	queue<POS> bfs_q{};
	bfs_q.push( { 0, 0 } );

	while ( not bfs_q.empty() ) {
		auto pos = bfs_q.front();
		bfs_q.pop();

		for ( int i{}; i < 4; ++i ) {
			int new_y{ pos.y + dirs[i].y };
			int new_x{ pos.x + dirs[i].x };

			if ( new_y < 0 or new_x < 0 or new_y >= param.n or new_x >= param.k )
				continue;

			if ( param.v[new_y][new_x] == MONSTER )
				continue;

			int& new_dist = min_dist[new_y][new_x];

			if ( new_dist == ROAD ) {
				new_dist = min_dist[pos.y][pos.x] + 1;
				bfs_q.push( { new_y, new_x } );
			}
		}
	}

	return min_dist.back().back();
}
