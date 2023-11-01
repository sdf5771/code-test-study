#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct Param {
	int n{}, k{};
	vector<pair<int, int>> v{};

	friend istream& operator>>( istream& is, Param& p )
	{
		is >> p.n >> p.k;

		int elm1{}, elm2{};
		for ( int i{}; i < p.n; ++i ) {
			is >> elm1 >> elm2;
			p.v.emplace_back( elm1, elm2 );
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

Result MySolution( Param param )	// wrong
{
	{
		auto itr = remove_if( param.v.begin(), param.v.end(), []( const auto& lhs ) {
			return lhs.second <= 0;
			} );
		param.v.erase( itr, param.v.end() );
	}

	vector<int> v_values( param.k + 1, 0 );	// 최대 무게에 따른 가치 최대값
	vector<vector<vector<int>>> v_indices( param.k + 1, vector<vector<int>>{} );	// DP Table, 무게에 따라 담을 물건의 index를 가짐
	v_indices[0].push_back( {} );	//

	for ( int i{ 1 }; i <= param.k; ++i ) {
		v_values[i] = v_values[i - 1];	// 이전 무게를 기준
		//v_indices[i] = v_indices[i - 1];

		for ( int j{}; j < param.v.size(); ++j ) {
			const int cur_w = param.v[j].first;		// 현 물건 무게
			const int cur_v = param.v[j].second;	// 현 물건 가치
			const int sub_i{ i - cur_w };			// 현 물건을 뺐을 때의 무게

			// 최대 무게보다 물건이 무거우면 무시
			if ( sub_i < 0 )
				continue;

			// 최대값이 되는 모든 경우의 수를 경유
			for ( int k{ -1 }; const auto & vi : v_indices[sub_i] ) {
				++k;

				// v_indices[sub_i]에 해당 index(j)가 있다면? 이미 가방에 싸놓은 상태, 무시.
				if ( find( vi.begin(), vi.end(), j ) != vi.end() )
					continue;

				// 가치가 가장 높은 경우'들' 찾기
				const int sum_v = v_values[sub_i] + cur_v;
				if ( v_values[i] <= sum_v ) {
					v_values[i] = sum_v;
					v_indices[i].push_back( vi );
					v_indices[i].back().emplace_back( j );
				}
			}

		}

		// 최댓값이 아닌 값들 제거
		{
			auto itr = remove_if( v_indices[i].begin(), v_indices[i].end(), [&]( const auto& lhs ) {
				int num = accumulate( lhs.begin(), lhs.end(), 0, [&]( const auto& lhs, const auto& rhs ) {
					return lhs + param.v[rhs].second;
					} );
				return num < v_values[i];
				} );

			v_indices[i].erase( itr, v_indices[i].end() );
		}

		// 중복배열 제거
		{
			for ( auto& v : v_indices[i] )
				sort( v.begin(), v.end() );
			sort( v_indices[i].begin(), v_indices[i].end() );


			auto itr = unique( v_indices[i].begin(), v_indices[i].end() );

			v_indices[i].erase( itr, v_indices[i].end() );
		}

	}

	return v_values.back();

	// 1 = 1 : 1
	// 2 = 2 : 2
	// 3 = 1, 2 : 3 | 3 : 3
	// 4 = 1, 3 : 4 | 4 : 4
	// 5 = 1, 4 : 5 | 2, 3 : 5 | 5 : 5
	// 6 = 1, 5 : 6 | 2, 4 : 6 | 1, 2, 3 : 6
	// 7 = 2, 5 : 7 | 3, 4 : 7

	// 201 = 98, 103 : 201 | 100, 101 : 201
	// ...
	// 203 = 98, 4, 101 : 203 | 100, 103 | 203
	// 204 = 98, 6, 100 : 204 | 101, 103 | 204
	// ...
	// 304 = 100, 101, 103 | 304
}

Result BookSolution( Param param )
{
	vector<vector<int>> dp( param.n + 1, vector<int>( param.k + 1, 0 ) );

	for ( int i{ 1 }; i < param.n + 1; ++i ) {
		for ( int j{ 1 }; j < param.k + 1; ++j ) {
			int weight{ param.v[i - 1].first };
			int value{ param.v[i - 1].second };

			dp[i][j] = dp[i - 1][j];
			
			if ( weight <= j )
				dp[i][j] = max( dp[i][j], value + dp[i - 1][j - weight] );

		}
	}

	return dp[param.n][param.k];
}