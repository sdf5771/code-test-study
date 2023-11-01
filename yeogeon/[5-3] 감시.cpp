#include <iostream>
#include <vector>
#include <array>
#include <numeric>

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
}

Result MySolution( Param param )
{
	// 
	using MAP = vector<vector<int>>;

	const static int BLANK{ 0 }, WALL{ 6 }, WATCHING{ 7 };	// 보인 곳은 7로 변경

	enum DIR { N, E, S, W, CNT };	// 방향

	struct POS { int y{}, x{}; };	// 위치 2D 벡터
	const static POS DIRS[]{ {-1, 0}, {0, 1}, {1, 0}, {0, -1} };	// 실제 방향 벡터

	struct CCTV {
		int num{};	// 종류(1~5)
		POS pos{};	// 위치
		array<bool, DIR::CNT> dirs{};	// 종류에 따른 방향
		CCTV* next{};	// 다음 CCTV(연결 리스트)

		CCTV() = default;
		CCTV( int num, POS pos, array<bool, DIR::CNT> dirs ) :
			num{ num }, pos{ pos }, dirs{ dirs } {}

		// 해당하는 방향 감시하기
		void Watch( MAP& map )
		{
			// 4방향 확인
			for ( DIR d{}; d < DIR::CNT; d = DIR( int( d ) + 1 ) ) {

				// 현 방향이 내 영역인가?
				if ( dirs[d] ) {
					POS np{ pos.y, pos.x };

					while ( true ) {
						// 바라보는 방향의 다음 칸(좌표)
						np = { np.y + DIRS[d].y, np.x + DIRS[d].x };

						// map 밖을 벗어나는가
						if ( np.y < 0 or np.y >= map.size() or np.x < 0 or np.x >= map.front().size() )
							break;

						// 6(벽)인가
						if ( map[np.y][np.x] == WALL )
							break;

						// 해당 위치는 감시중
						map[np.y][np.x] = WATCHING;
					}
				}
			}
		}

		// 회전시키기
		void Rotate( int cnt )
		{
			// bool[4]를 한 칸씩 미는 방식
			// 예) ( T, F, F, F ) -> ( F, T, F, F )
			rotate( dirs.begin(), dirs.begin() + cnt, dirs.end() );
		}

		// DFS로 모든 노드와의 경우의 수 확인 (map은 복사)
		// 예) 1[W], 2[W]: 5, 1[W], 2[E]: 3 ...
		void WatchDFS( MAP map, int& min_bs ) {

			// CCTV마다 최소 회전 수가 달라서 미미한 최적화를 해보았음
			int iter{};
			switch ( num ) {
			case 1:
			case 3:
			case 4:
				iter = 4;
				break;
			case 2:
				iter = 2;
				break;
			case 5:
				iter = 1;
			}

			// 회전 수 만큼만 반복
			for ( int i{}; i < iter; ++i ) {
				// 위 단계에서 받은 map을 복사
				MAP tmp_map{ map };

				// 감시는 레퍼런싱으로 map을 변경하도록
				Watch( tmp_map );

				// 노드가 끝났다면? (next == end)
				if ( not next ) {

					// 최종적으로 만들어진 map의 사각지대 수를 구함
					int cnt = accumulate( tmp_map.begin(), tmp_map.end(), 0, []( const int& lhs, auto& rhs ) {
						return lhs + accumulate( rhs.begin(), rhs.end(), 0, []( const int& lhs, auto& rhs ) {
							return lhs + ( rhs == BLANK ? 1 : 0 );
							} );
						} );

					// 최소값(레퍼런스)와 방금 전의 사각지대의 수 중 더 적은 값을 min_bs에 할당
					min_bs = min( min_bs, cnt );
				}
				else
					// 다음 노드(CCTV)가 있다면 해당 CCTV의 감시 영역을 확인
					next->WatchDFS( tmp_map, min_bs );

				// 한 바퀴 회전
				Rotate( 1 );
			}

		}
	};

	// 최소값은 map의 크기
	Result min_bs{ param.n * param.k };

	// CCTV 리스트
	CCTV* CCTVs{};

	for ( int y{}; y < param.n; ++y )
		for ( int x{}; x < param.k; ++x ) {
			int i = param.v[y][x];
			array<bool, DIR::CNT> tmp_dirs{};

			// CCTV 종류별로 보는 방향을 정해준다.
			switch ( i ) {
			case 1:
				tmp_dirs = { false, true, false, false };	// E
				break;
			case 2:
				tmp_dirs = { false, true, false, true };	// E W
				break;
			case 3:
				tmp_dirs = { true, true, false, false };	// N E
				break;
			case 4:
				tmp_dirs = { true, true, true, false };		// N E S
				break;
			case 5:
				tmp_dirs = { true, true, true, true };		// N E S W
				break;
			default:
				continue;
			}

			// 리스트에 추가
			CCTV* new_cctv{ new CCTV{ i, {y, x}, tmp_dirs } };

			if ( not CCTVs )
				CCTVs = new_cctv;
			else {
				new_cctv->next = CCTVs;
				CCTVs = new_cctv;
			}
		}

	// CCTV가 한 개 이상 있다면 탐색 시작
	if ( CCTVs != nullptr )
		CCTVs->WatchDFS( param.v, min_bs );

	// CCTV가 없다면 빈 칸을 찾아줌
	else {
		int cnt = accumulate( param.v.begin(), param.v.end(), 0, []( const int& lhs, auto& rhs ) {
			return lhs + accumulate( rhs.begin(), rhs.end(), 0, []( const int& lhs, auto& rhs ) {
				return lhs + ( rhs == BLANK ? 1 : 0 );
				} );
			} );

		min_bs = min( min_bs, cnt );
	}

	return min_bs;
}

Result BookSolution( Param param )
{
	return 0;
}