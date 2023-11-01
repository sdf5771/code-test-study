#include <iostream>
#include <vector>
#include <algorithm>
#include "CodingTester.h"

using namespace std;

struct Param {
	int n{}, k{};
	int y{}, x{}, d{};
	vector<vector<int>> map;

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n >> p.k;
		is >> p.y >> p.x >> p.d;

		for ( int i{}; i < p.k; ++i ) {
			p.map.push_back( {} );
			for ( int j{}; j < p.n; ++j ) {
				int num{};
				is >> num;
				p.map[i].push_back( num );
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
}

enum DIR { N, E, S, W, DIR_CNT };

DIR& operator--( DIR& dir ) {
	dir = static_cast<DIR>( ( static_cast<int>( dir ) - 1 + DIR_CNT ) % DIR_CNT );
	return dir;
};

DIR& operator-( DIR& dir, int dec ) {
	DIR d = static_cast<DIR>( ( static_cast<int>( dir ) - dec + DIR_CNT ) % DIR_CNT );
	return d;
}

struct POS {
	int y{}, x{};

	bool operator==( const POS& pos ) const {
		return ( y == pos.y ) && ( x == pos.x );
	}
};

Result MySolution( Param param )
{
	Result cnt{ 1 };

	constexpr int LAND{ 0 }, SEA{ 1 };
	POS dirs[]{ {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

	POS cur_pos{ param.y, param.x };
	DIR cur_dir{ DIR( param.d ) };
	DIR first_dir{ cur_dir };

	vector<POS> stepped_lands{ cur_pos };

	while ( true ) {
 		DIR new_dir{ cur_dir - 1 };	// 반시계방향으로 회전
		POS new_pos{};

		if ( new_dir == first_dir ) {	// 네 방향 모두 갈 수 없다면
			----new_dir;
			new_pos = { cur_pos.y + dirs[new_dir].y, cur_pos.x + dirs[new_dir].x };

			if ( param.map[new_pos.y][new_pos.x] == LAND )	// 뒤로 갈 수 있다면
				cur_pos = new_pos;
			else // 뒤가 바다라면
				break;
			
			cur_dir = first_dir;
			continue;	// 다시 1단계로
		}

		new_pos = { cur_pos.y + dirs[new_dir].y, cur_pos.x + dirs[new_dir].x };

		if ( param.map[new_pos.y][new_pos.x] == LAND ) {	// 육지를 발견한다면
			if ( find( stepped_lands.begin(), stepped_lands.end(), new_pos ) == stepped_lands.end() ) {	// 방문한 적도 없다면
				++cnt;
				cur_dir = first_dir = new_dir;
				cur_pos = new_pos;
				stepped_lands.push_back( new_pos );
			}
		}

		cur_dir = new_dir;
		// 다시 1단계로
	}

	return cnt;
}

Result BookSolution( Param param )
{
	return Result{};
}
